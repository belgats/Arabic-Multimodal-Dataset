 
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
        
        with open(os.path.join(text_embedding, f'{vid_key}'), 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            print(reader)
            for i, row in enumerate(reader):
                row_np = np.array([ f'{float(cell):.9e}' for cell in row], dtype=np.float64)
                # Append the numpy array to the list
                features.append(row_np)
            compseq[vid_key]["features"]=  np.array(features)
            print(compseq[vid_key]["features"].shape)


if __name__=="__main__":
    compseq_TimeWord_data={}
    #let's assume compseq_1 is some modality with a random feature dimension
    Generate_ComSeq(compseq_TimeWord_data,config.vid_keys)
    compseq_TimestampedWordVectors=mmdatasdk.computational_sequence("TimestampedWordVectors")
    compseq_TimestampedWordVectors.setData(compseq_TimeWord_data,"TimestampedWordVectors")
    #NOTE: if you don't want to manually input the metdata, set it by creating a metdata key-value dictionary based on mmsdk/mmdatasdk/configurations/metadataconfigs.py
    compseq_TimestampedWordVectors.deploy("MMAD_TimestampedWordVectors.csd")