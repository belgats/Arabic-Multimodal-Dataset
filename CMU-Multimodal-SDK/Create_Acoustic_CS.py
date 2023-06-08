import mmsdk
from mmsdk import mmdatasdk
import numpy as np
import os
import csv
 

import config
from tqdm import tqdm


# Define files path
audio_root = config.PATH_TO_RAW_AUDIO[config.DATA_DIR['MMAD']]  
text_root  = config.PATH_TO_TEXT_VECTORS[config.DATA_DIR['MMAD']]  
video_root = config.PATH_TO_RAW_VIDEO[config.DATA_DIR['MMAD']] 
annotation_root = config.PATH_TO_RAW_ANNOATION[config.DATA_DIR['MMAD']] 

def Generate_ComSeq(compseq, Alined_items):
    
    for vid_key in tqdm(Alined_items, desc="Processing audio", unit="audio"):
        compseq[vid_key]={} 
        intervals= []
        features= []
 
        file_path = os.path.join(audio_root, f'{vid_key}.csv') 
        
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                row_np = np.array([  f'{float(val):.9e}' for val in row[2:]], dtype=np.float64)
                features.append(row_np)
                row_interval = np.array([ f'{float(row[1]):.9e}', f'{float(row[1])+ 0.01:.9e}'], dtype=np.float64)
                intervals.append(row_interval)
            # Convert the list of numpy arrays to a numpy array
            compseq[vid_key]["features"]= np.array(features)
            compseq[vid_key]["intervals"]=  np.array(intervals)
 
 
if __name__=="__main__":

    compseq_OpenSmiles_features={}
    #let's assume compseq_1 is some modality with a random feature dimension
    Generate_ComSeq(compseq_OpenSmiles_features,config.vid_keys)
    compseq_OpenSmiles=mmdatasdk.computational_sequence("MMAD_OpenSmile")
    compseq_OpenSmiles.setData(compseq_OpenSmiles_features,"MMAD_OpenSmile")
    #NOTE: if you don't want to manually input the metdata, set it by creating a metdata key-value dictionary based on mmsdk/mmdatasdk/configurations/metadataconfigs.py
    compseq_OpenSmiles.deploy("MMAD_acoustic.csd")
  