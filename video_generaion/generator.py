import subprocess
from pydub import AudioSegment


#todo: not working at all
def generate(args):
    lr = lambda *x: list(range(*x))
    a = 0
    for i, j in enumerate(sentences):
        time = 10
        frs = time * 30
        # 300
        # 400 sp * 2 = 800
        # первые 200 каждая 4я = 50
        # следующие 100 каждая 2я = 50
        # следующие 100 каждая = 100
        # потом 400 каждая 4я = 100
        path = f"../aiijc-creative-imagegen/steps/steps/{i}/"
        data = lr(0, 200, 4) + lr(200, 300, 2) + lr(300, 400, 1) + lr(399, -1, -4)
        for k in data:
            subprocess.run(f"cp {path}frame_{str(k).zfill(4)}.png ../ready/here_{a}.png", shell=True)
            a += 1


    final = AudioSegment.silent(0)

    for i, j in tqdm(enumerate(sentences)):
        fn = f"""output/result/LibriTTS/{j.replace('"', ' ')}.wav"""
        seg = AudioSegment.from_file(fn, format="wav")
        sil_duration = (6000 - len(seg)) / 2
        silence = AudioSegment.silent(sil_duration)
        final += silence + seg + silence
    music = AudioSegment.from_file("item_2.wav", format="wav")[4000:]

    music = music + music + music + music + music + music + music + music + music
    music = music[:len(final)]
    final = final.overlay(music, position=0)
    final = final[:300 * 36 * 1000 // 50]
    print(len(final))
    final.export("../audio/ready.wav", format="wav")

    subprocess.run("ffmpeg -i ../audio/ready.wav -framerate 50  -i here_%d.png -q:v 6 video_name.avigit ")
