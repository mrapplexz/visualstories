from helper import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt', metavar='P', type=str, nargs='+',  help='text prompt')
    args = parser.parse_args()
    prompt = ' '.join(args.prompt)

    print(f"Generating text for prompt `{prompt}`")

    import_stuff()

    import pixray

    pixray.reset_settings()
    pixray.add_settings(prompts=f"{prompt} #pixelart", aspect='widescreen')
    pixray.add_settings(quality="better", scale=2.5)
    pixray.add_settings(drawer='pixeldraw')
    pixray.add_settings(display_clear=True)
    pixray.add_settings(make_frames=True)

    settings = pixray.apply_settings()
    pixray.do_init(settings)
    pixray.do_run(settings)
