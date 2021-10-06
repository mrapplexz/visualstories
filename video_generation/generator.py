import os
import subprocess
from pydub import AudioSegment
from tqdm import tqdm

def generate(args):
    print("Preparing frames")
    os.makedirs(f"{args.temp_dir}/prepared_frames", exist_ok=True)
    frame_dirs = os.listdir(args.frame_dir)
    lr = lambda *x: list(range(*x))
    time = 6  # time of every picture
    total_time_in_ms = len(frame_dirs) * time * 1000
    frs = time * 50
    # we need 300 frames
    # but we have 400 * 2 = 800
    # first 200 every 4th = 50
    # next 100 every 2nd = 50
    # next 100 every 1st = 100
    # then reverse 400 every 4th = 100
    frame_enumeration = lr(0, 200, 4) + lr(200, 300, 2) + lr(300, 400, 1) + lr(399, -1, -4)
    frame_index = 0
    for fd in tqdm(frame_dirs):
        path = f"{args.frame_dir}/{fd}"
        for local_frame_index in frame_enumeration:
            subprocess.run(
                f"cp {path}/frame_{str(local_frame_index).zfill(4)}.png {args.temp_dir}/prepared_frames/new_frame_{frame_index}.png",
                shell=True)
            frame_index += 1

    final_audio = AudioSegment.silent(0)

    print("Preparing tts")
    for i in tqdm(range(len(frame_dirs))):
        fn = f"""{args.tts_dir}/tts_{i}.wav"""
        seg = AudioSegment.from_file(fn, format="wav")
        sil_duration = (time * 1000 - len(seg)) / 2
        silence = AudioSegment.silent(sil_duration)
        final_audio += silence + seg + silence  # left and right padding for exact time

    music = AudioSegment.from_file(f"{args.music_filename}", format="wav") + args.music_corrector

    final_audio = final_audio.overlay(music, position=0, loop=True)
    final_audio = final_audio[:total_time_in_ms]

    audio_path = f"{args.temp_dir}/final_audio.wav"
    final_audio.export(audio_path, format="wav")

    frame_path = f"{args.temp_dir}/prepared_frames/new_frame_%d.png"
    subprocess.run(f"ffmpeg -i {audio_path} -framerate 50  -i {frame_path} -q:v {args.quality} {args.video_name}", shell=True)
