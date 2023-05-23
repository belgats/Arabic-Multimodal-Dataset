#!/bin/bash

# Define the Opensmile task options
conf="../../../config/emobase/emobase.conf"

# Loop over the 10 files
for i in {1..60}; do
    # Define the input and output file names
    mp3_file="${i}.wav"
    tsv_file="./${i}.csv"

    # Run the opensmile task for the current input files

    ./SMILExtract -C  "$conf" -I "../../../$mp3_file" -lldcsvoutput  "$tsv_file"

done
