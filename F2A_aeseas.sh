#!/bin/bash

# Define the Aeneas task options
aeneas_options="task_language=ar|os_task_file_format=tsv|is_text_type=plain"
aeneas_presets="--presets-word -r='tts=espeak-ng|allow_unlisted_languages=true'"

# Loop over the 10 files
for i in {1..60}; do
    # Define the input and output file names
    mp3_file="${i}.mp3"
    txt_file="${i}.txt"
    tsv_file="${i}.tsv"

    # Run the Aeneas task for the current input files
    python -m aeneas.tools.execute_task "$mp3_file" "$txt_file" "$aeneas_options" "$tsv_file" $aeneas_presets
done
