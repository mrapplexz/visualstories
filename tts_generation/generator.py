import subprocess


def generate(args):
    for i, line in enumerate(open(f"{args.temp_dir}/source.txt")):
        generation_command = f"""cd tts_generation/FastSpeech2                                               \
                                 &&                                                                          \
                                 ../tts_generation_env/bin/python3                                           \
                                 synthesize.py                                                               \
                                 --mode single                                                               \
                                 --text "{line.strip()}"                                                     \
                                 --speaker_id {args.speaker_id}                                              \
                                 --restore_step 800000                                                       \
                                 -p config/LibriTTS/preprocess.yaml                                          \
                                 -m config/LibriTTS/model.yaml                                               \
                                 -t config/LibriTTS/train.yaml                                               \
                                 &&                                                                          \
                                 cd ../..                                                                    \
                                 &&                                                                          \
                                 mv "tts_generation/FastSpeech2/output/result/LibriTTS/{line.strip()}.wav"   \
                                 {args.output_dir}/tts_{i}.wav"""
        subprocess.run(generation_command, shell=True)
    subprocess.run("rm tts_generation/FastSpeech2/output/result/LibriTTS/*", shell=True)
