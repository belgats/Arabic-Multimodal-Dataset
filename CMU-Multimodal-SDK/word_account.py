import config
 
g_acount = 0
# Loop over all the files and count the words in each file
for file_name in config.vid_keys:
    with open( "~/Downloads/dataset/" + file_name+".txt", 'r') as file:
        contents = file.read()
        words = contents.split()
        num_words = len(words)
        g_acount += g_acount+num_words
        print("The file '{}' contains {} words.".format(file_name, num_words))

print("Global numbers {} words.".format( g_acount))        