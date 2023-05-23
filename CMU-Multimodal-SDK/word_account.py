# Create a list of file names
file_names = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt", 
              "6.txt", "7.txt", "8.txt", "9.txt", "10.txt","11.txt", "12.txt", "13.txt", "14.txt", "15.txt",
              "16.txt", "17.txt", "18.txt", "19.txt", "20.txt","21.txt", "22.txt", "23.txt", "24.txt", "25.txt",
              "26.txt", "27.txt", "28.txt", "29.txt", "30.txt","31.txt", "32.txt", "33.txt", "34.txt", "35.txt",
              "36.txt", "37.txt", "38.txt", "39.txt", "40.txt","41.txt", "42.txt", "43.txt", "44.txt", "45.txt",
              "46.txt", "47.txt", "48.txt", "49.txt", "50.txt","51.txt", "52.txt", "53.txt", "54.txt", "55.txt",
              "56.txt", "57.txt", "58.txt", "59.txt", "60.txt"]

g_acount = 0
# Loop over all the files and count the words in each file
for file_name in file_names:
    with open( "~/Downloads/dataset/" + file_name, 'r') as file:
        contents = file.read()
        words = contents.split()
        num_words = len(words)
        g_acount += g_acount+num_words
        print("The file '{}' contains {} words.".format(file_name, num_words))

print("Global numbers {} words.".format( g_acount))        
