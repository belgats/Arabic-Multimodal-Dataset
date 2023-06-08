 
import mmsdk
from mmsdk import mmdatasdk
import numpy as np
import os
import csv


from tqdm import tqdm

import config

# Define files path
audio_root = config.PATH_TO_RAW_AUDIO[config.DATA_DIR['MMAD']]  
text_root  = config.PATH_TO_TEXT_VECTORS[config.DATA_DIR['MMAD']]  
video_root = config.PATH_TO_RAW_VIDEO[config.DATA_DIR['MMAD']] 

def Generate_ComSeq(compseq, Alined_items): 
    
    for vid_key in tqdm(Alined_items, desc="Processing transciptions", unit="word"):
        
        compseq[vid_key]={} 
        intervals= []
        features= []
        file_path = os.path.join(text_root, f'{vid_key}.csv')
        with open( file_path, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            print(reader)
            for i, row in enumerate(reader):
                row_np = np.array([ f'{float(row[0]):.9e}',  f'{float(row[1]):.9e}'], dtype=np.float64)
                # Append the numpy array to the list
                intervals.append(row_np)
            # Convert the list of numpy arrays to a numpy array
            compseq[vid_key]["intervals"]= np.array(intervals)
            #print(compseq[vid_key]["intervals"][0].shape)

        with open(os.path.join(text_root, f'{vid_key}.txt'), 'r') as file:
            
            lines = file.readlines()
            for line in lines:
                 words_np = np.array([line.strip().encode('utf-8') ], dtype='|S15')
                 features.append(words_np)
            compseq[vid_key]["features"]=  np.array(features)
            #print(compseq[vid_key]["features"][0].shape)

 

if __name__=="__main__":

    compseq_Words_data={}
    #let's assume compseq_1 is some modality with a random feature dimension
    Generate_ComSeq(compseq_Words_data,config.vid_keys)
    compseq_TimestampedWords=mmdatasdk.computational_sequence("TimestampedWords")
    compseq_TimestampedWords.setData(compseq_Words_data,"TimestampedWords")
    #NOTE: if you don't want to manually input the metdata, set it by creating a metdata key-value dictionary based on mmsdk/mmdatasdk/configurations/metadataconfigs.py
    compseq_TimestampedWords.deploy("MMAD_TimestampedWord.csd")