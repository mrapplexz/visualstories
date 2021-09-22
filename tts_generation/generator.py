import subprocess


def generate(args):
    generation_command = f"""python3
                            synthesize.py 
                            --mode batch 
                            --source {args.temp_filename}
                            --speaker_id {args.speaker_id} 
                            --restore_step 800000
                            -p FastSpeech2/config/LibriTTS/preprocess.yaml 
                            -m FastSpeech2/config/LibriTTS/model.yaml
                            -t FastSpeech2/config/LibriTTS/train.yaml"""
    subprocess.run(generation_command)

    for i, line in enumerate(open(args.temp_filename).readlines()):
        renaming_comand = f"""mv ./FastSpeech2/output/result/LibriTTS/{line.strip()}.wav {args.output_dir}/tts_{i}.wav"""
        subprocess.run(renaming_comand)
