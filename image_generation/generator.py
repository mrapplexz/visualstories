from helper import *
import argparse


def setup():
    import_stuff()


def generate(prompt, part_n, device):
    import pixray
    pixray.reset_settings()
    pixray.add_settings(prompts=f"{prompt} #pixelart", part_n=part_n, device=device)
    pixray.add_settings(aspect='widescreen', quality="better", scale=2.5)
    pixray.add_settings(drawer='pixeldraw')
    pixray.add_settings(display_clear=True)
    pixray.add_settings(make_frames=True)

    settings = pixray.apply_settings()
    pixray.do_init(settings)
    pixray.do_run(settings)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--part_n", type=int, help="Part number to save", default=0, dest='part_n')
    parser.add_argument("--device", type=str, help="Device to use", default=None, dest='device')
    parser.add_argument('prompt', metavar='P', type=str, nargs='+',  help='text prompt')
    args = parser.parse_args()
    text_prompt = ' '.join(args.prompt)

    setup()

    print(f"Generating text for prompt `{text_prompt}`")
    generate(text_prompt, args.part_n, args.device)
