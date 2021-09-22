import argparse
from text_generation.generator import generate
from text_generation.config import available_genres

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('device', type=str, default="cuda:0", help='device to use')
    parser.add_argument('output_filename', type=str, default="./texts/text.txt", help='destination of ready text')
    parser.add_argument('temperature', type=float, default=0.1, help='temperature for generation')
    parser.add_argument('top_k', type=int, default=10000, help='top_k for generation')
    parser.add_argument('top_p', type=float, default=0.95, help='top_p for generation')
    parser.add_argument('repetition_penalty', type=float, default=5., help="repetition_penalty for generation")
    parser.add_argument('max_length', type=int, default=1000, help="length for generation")
    parser.add_argument('seed', type=int, default=42, help="length for generation")
    parser.add_argument('start', type=str, default="", help="start of the desired story")
    parser.add_argument('genre', type=str, default="fairy_tale", help="genre of the desired story",
                        choices=available_genres.keys())
    args = parser.parse_args()
    text = generate(args)
    open(args.output_filename, "w").write(text)
