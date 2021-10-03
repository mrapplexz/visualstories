import argparse
from tts_generation.generator import generate
from utils import preprocess_prompt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_filename', type=str, default="./output/texts/text.txt",
                        help='destination of ready text', dest="input_filename")
    parser.add_argument('--temp_filename', type=str, default="./tmp/source.txt",
                        help='destination of temp text', dest="temp_filename")
    parser.add_argument('--speaker_id', type=int, default=205,
                        help='LibriTTS speaker id', dest="speaker_id")
    parser.add_argument('--output_dir', type=str, default="./output/tts",
                        help="directory for saving speech wavs", dest="output_dir")
    args = parser.parse_args()
    prompts = preprocess_prompt(open(args.input_filename).read())
    open(args.temp_filename, "w").write("\n".join(prompts))
    generate(args)
