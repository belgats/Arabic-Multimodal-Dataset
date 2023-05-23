#!/bin/bash

# Define the Aeneas task options
aeneas_options="task_language=ar|os_task_file_format=tsv|is_text_type=plain"
aeneas_presets="--presets-word -r='tts=espeak-ng|allow_unlisted_languages=true'"

# Loop over the 10 files
for i in {0..60}; do
    # Define the input and output file names
    mp4_file="${i}.mp4"
    output_file="${i}.wav"
    ffmpeg -i "$mp4_file" -acodec pcm_s16le -ar 44100 "$output_file"
    # Run the Aeneas task for the current input files
   
done
