import argparse

from image_generation.helper import import_stuff
from image_generation.generator_parallel import generate_parallel
from utils import preprocess_prompt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt_file', type=str, help='text prompt file')
    parser.add_argument('devices', type=str, help='list of devices e.g. cuda:0,cuda:2,cpu')
    parser.add_argument('main_dir', type=str, help='directory to save pictures')
    args = parser.parse_args()
    devices = args.devices.split(",")
    prompts = preprocess_prompt(open(args.prompt_file).read())
    main_dir = args.main_dir
    import_stuff()
    generate_parallel(prompts, devices, main_dir)
