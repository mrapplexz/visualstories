from multiprocessing import Queue, current_process, Pool, Manager

from generator import generate


def generate_parallel_worker(free_gpus, text, n):
    device = free_gpus.get()
    try:
        ident = current_process().ident
        print(f'{ident}: starting process on device {device}')
        generate(text, n, device)
        print(f'{ident}: finished')
    finally:
        free_gpus.put(device)


def generate_parallel(prompts, devices):
    print('Starting parallel training...')
    mgr = Manager()
    free_gpus = mgr.Queue()
    for device in devices:
        free_gpus.put(device)
    pool = Pool(len(devices))
    results = [pool.apply_async(generate_parallel_worker, (free_gpus, prompt, i)) for i, prompt in enumerate(prompts)]
    for result in results:
        result.wait()
    print('Done all the work!')