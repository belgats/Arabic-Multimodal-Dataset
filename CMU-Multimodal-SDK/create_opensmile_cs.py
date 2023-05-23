import mmsdk
from mmsdk import mmdatasdk
import numpy as np
import os
import csv
 

text_Aligned = "/home/slasher/Downloads/dataset/text_Aligned/"
opensmile = "/home/slasher/Downloads/dataset/V2/opensmile/"
openface = "/home/slasher/Downloads/dataset/V2/Openface/"
text_embedding = "/home/slasher/Downloads/dataset/text_embedding/"

def OpenSmiles_data(compseq, Alined_items):
    
    for vid_key in Alined_items:
        title=vid_key
        title = title[:-4]
        compseq[title]={} 
        intervals= []
        features= []
         
        print(os.path.join(opensmile, f'{vid_key}'))
        with open(os.path.join(opensmile, f'{vid_key}'), 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                row_np = np.array([  f'{float(val):.9e}' for val in row[2:]], dtype=np.float64)
                features.append(row_np)
                print(row[2:])
                row_interval = np.array([ f'{float(row[1]):.9e}', f'{float(row[1])+ 0.01:.9e}'], dtype=np.float64)
                intervals.append(row_interval)
            # Convert the list of numpy arrays to a numpy array
            compseq[title]["features"]= np.array(features)
            compseq[title]["intervals"]=  np.array(intervals)
 
 
if __name__=="__main__":
    vid_keys=["1","2","3","4","5","6","7","8","9","10","11", "12",  "13",  "14",  "15",  "16",  "17",  "18",  "19",  "20","21", "22",  "23",  "24",  "25",  "26",  "27",  "28",  "29",  "30","31", "32",  "33",  "34",  "35",  "36",  "37",  "38",  "39",  "40"]
    vid_Files=["1.txt", "2.txt",  "3.txt",  "4.txt",  "5.txt",  "6.txt",  "7.txt",  "8.txt",  "9.txt",  "10.txt","11.txt", "12.txt",  "13.txt",  "14.txt",  "15.txt",  "16.txt",  "17.txt",  "18.txt",  "19.txt",  "20.txt","21.txt", "22.txt",  "23.txt",  "24.txt",  "25.txt",  "26.txt",  "27.txt",  "28.txt",  "29.txt",  "30.txt","31.txt", "32.txt",  "33.txt",  "34.txt",  "35.txt",  "36.txt",  "37.txt",  "38.txt",  "39.txt",  "40.txt"]
    text_alined=["1.tsv", "2.tsv",  "3.tsv",  "4.tsv",  "5.tsv",  "6.tsv",  "7.tsv",  "8.tsv",  "9.tsv",  "10.tsv","11.tsv", "12.tsv",  "13.tsv",  "14.tsv",  "15.tsv",  "16.tsv",  "17.tsv",  "18.tsv",  "19.tsv",  "20.tsv","21.tsv", "22.tsv",  "23.tsv",  "24.tsv",  "25.tsv",  "26.tsv",  "27.tsv",  "28.tsv",  "29.tsv",  "30.tsv","31.tsv", "32.tsv",  "33.tsv",  "34.tsv",  "35.tsv",  "36.tsv",  "37.tsv",  "38.tsv",  "39.tsv",  "40.tsv"]
    openface1=["1.csv", "2.csv",  "3.csv",  "4.csv",  "5.csv",  "6.csv",  "7.csv",  "8.csv",  "9.csv",  "10.csv","11.csv", "12.csv",  "13.csv",  "14.csv",  "15.csv",  "16.csv",  "17.csv",  "18.csv",  "19.csv",  "20.csv","21.csv", "22.csv",  "23.csv",  "24.csv",  "25.csv",  "26.csv",  "27.csv",  "28.csv",  "29.csv",  "30.csv","31.csv", "32.csv",  "33.csv",  "34.csv",  "35.csv",  "36.csv",  "37.csv",  "38.csv",  "39.csv",  "40.csv"]
    openface=["11.csv", "12.csv",  "13.csv",  "14.csv",  "15.csv",  "16.csv",  "17.csv",  "18.csv",  "19.csv",  "20.csv","21.csv", "22.csv",  "23.csv",  "24.csv",  "25.csv",  "26.csv",  "27.csv",  "28.csv",  "29.csv",  "30.csv","31.csv", "32.csv",  "33.csv",  "34.csv",  "35.csv",  "36.csv",  "37.csv",  "38.csv",  "39.csv",  "40.csv"]
    compseq_OpenSmiles_data={}
    #let's assume compseq_1 is some modality with a random feature dimension
    OpenSmiles_data(compseq_OpenSmiles_data,openface)
    compseq_OpenSmiles=mmdatasdk.computational_sequence("MMAD_OpenSmile")
    compseq_OpenSmiles.setData(compseq_OpenSmiles_data,"MMAD_OpenSmile")
    #NOTE: if you don't want to manually input the metdata, set it by creating a metdata key-value dictionary based on mmsdk/mmdatasdk/configurations/metadataconfigs.py
    compseq_OpenSmiles.deploy("MMAD_OpenSmile30.csd")
  