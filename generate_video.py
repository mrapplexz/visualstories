from video_generaion.generator import generate
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame_dir', type=str, default="./output/frames",
                        help='destination of frames', dest="frame_dir")
    parser.add_argument('--tts_dir', type=str, default="./output/tts",
                        help='destination of tts', dest="tts_dir")
    parser.add_argument('--music_filename', type=str, default="./output/music/item_0.wav",
                        help='destination of music', dest="music_filename")
    parser.add_argument('--temp_dir', type=str, default="./tmp",
                        help='temp directory', dest="temp_dir")
    parser.add_argument('--video_name', type=str, default="./output/video/video.avi",
                        help='output file name', dest="video_name")
    parser.add_argument('--quality', type=int, default=6,
                        help='output file quality', dest="quality")
    parser.add_argument('--music_corrector', type=int, default=-4,
                        help='corrector of music level', dest="music_corrector")
    args = parser.parse_args()
    generate(args)
