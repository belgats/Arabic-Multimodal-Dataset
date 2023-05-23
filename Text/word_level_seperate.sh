#!/bin/bash

# Create an array of file names

# Initialize the global count variable
g_acount=0

for i in {11..40}; do

# Loop over all the files in the directory


    # Replace all spaces with newlines and save to a temporary file
    tr ' ' '\n' < "$i.mp3.txt" > "$i.tmp"
    # Replace the original file with the modified file
    mv "$i.tmp" "$i.txt"




# Loop over all the files and count the words in each file

    # Read the contents of the file and count the words
    num_words=$(cat "$i.txt" | wc -w)
    g_acount=$((g_acount + num_words))
    echo "The file '$i.txt' contains $num_words words."
done
# Print the global word count
echo "Global numbers $g_acount words."


