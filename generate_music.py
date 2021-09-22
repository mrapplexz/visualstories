import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for music generation')

    parser.add_argument("music_genre", type=str, help="set music genre")
    parser.add_argument("artist", type=str, help="set artist name")
    parser.add_argument("save_path", type=str, default="./music", help="path to save music")
    parser.add_argument("sample_len", type=int, default=30, help="length of melody in seconds")

    args = parser.parse_args()
