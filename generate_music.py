import argparse
from music_generation.generator import generate

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for music generation')

    parser.add_argument("--music_genre", type=str, help="set music genre", dest="music_genre")
    parser.add_argument("--artist", type=str, help="set artist name", dest="artist")
    parser.add_argument("--save_path", type=str, default="./output/music", help="path to save music", dest="save_path")
    parser.add_argument("--sample_len", type=int, default=30, help="length of melody in seconds", dest="sample_len")

    args = parser.parse_args()
    generate(args)
