from video_generaion.generator import generate
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('frame_dir', type=str, default="./frames", help='destination of frames')
    parser.add_argument('tts_dir', type=str, default="./tts", help='destination of tts')
    parser.add_argument('music_dir', type=str, default="./music", help='destination of music')
    parser.add_argument('temp_dir', type=str, default="./tmp/prepared_frames", help='temp directory for frames')
    parser.add_argument('video_name', type=str, default="./video/video.avi", help='output file name')
    args = parser.parse_args()
    generate(args)

