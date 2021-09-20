import os
import typing
from subprocess import Popen


def generate_timestamps(video_parts: typing.List[typing.Tuple[float, int]], out_file: str, transition_duration: float):
    with open(out_file, 'w') as f:
        for duration, part_n in video_parts:
            files = [f'steps/{part_n}/{x}' for x in os.listdir(f'steps/{part_n}')]
            transition_step = transition_duration / len(files)
            for file in files:
                f.write(f"file '{file}'\n")
                f.write(f"duration {transition_step}\n")
            f.write(f"file '{files[-1]}'\n")
            f.write(f"duration {duration - transition_duration * 2}\n")
            for file in files[::-1]:
                f.write(f"file '{file}'\n")
                f.write(f"duration {transition_step}\n")


def generate_video(timestamps_file: str, output_file: str, fps: int):
    p = Popen(['ffmpeg',
               '-y',
               '-f', 'concat',
               '-i', timestamps_file,
               '-vcodec', 'libx264',
               '-r', str(fps),
               '-pix_fmt', 'yuv420p',
               '-preset', 'veryslow',
               output_file])
    p.wait()


def upscale_video(input_file: str, output_file: str, target_width: int, target_height: int):
    p = Popen(['ffmpeg',
               '-y',
               '-i', input_file,
               '-vf', f'scale={target_width}:{target_height}:flags=neighbor',
               output_file])
    p.wait()


if __name__ == '__main__':
    generate_timestamps([(5, 105), (2, 106), (10, 102), (4, 103)], 'output.txt', 0.4)
    generate_video('output.txt', 'output.mp4', 60)
    upscale_video('output.mp4', 'output_up.mp4', 7680, 4320)
