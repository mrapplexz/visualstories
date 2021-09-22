import argparse
from tts_generation.generator import generate
from utils import preprocess_prompt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename', type=str, default="./texts/text.txt", help='destination of ready text')
    parser.add_argument('temp_filename', type=str, default="./tmp/source.txt", help='destination of temp text')
    parser.add_argument('speaker_id', type=int, default=205, help='LibriTTS speaker id')
    parser.add_argument('output_dir', type=str, default="./tts", help="directory for saving speech wavs")
    args = parser.parse_args()
    prompts = preprocess_prompt(open(args.prompt_file).read())
    open(args.temp_filename, "w").write("\n".join(prompts))
    generate(args)
