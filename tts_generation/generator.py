import subprocess

#todo: doesn't work, rewrite to single mode
def generate(args):
    generation_command = f"""cd tts_generation/FastSpeech2                                        \
                             &&                                                                   \
                             ../tts_generation_env/bin/python3                                    \
                             synthesize.py                                                        \
                             --mode batch                                                         \
                             --source ../../{args.temp_filename}                                        \
                             --speaker_id {args.speaker_id}                                       \
                             --restore_step 800000                                                \
                             -p config/LibriTTS/preprocess.yaml                                   \
                             -m config/LibriTTS/model.yaml                                        \
                             -t config/LibriTTS/train.yaml                                        \
                             &&                                                                   \
                             cd ../.."""
    subprocess.run(generation_command, shell=True)

    for i, line in enumerate(open(args.temp_filename).readlines()):
        renaming_comand = f"""mv ./tts_generation/FastSpeech2/output/result/LibriTTS/{line.strip()}.wav {args.output_dir}/tts_{i}.wav"""
        subprocess.run(renaming_comand, shell=True)
