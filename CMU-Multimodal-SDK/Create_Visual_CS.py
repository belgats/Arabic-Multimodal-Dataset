import mmsdk
from mmsdk import mmdatasdk
import numpy as np
import os
import csv
 
#log is the same as standard_sdks log
from mmsdk.mmdatasdk import log 
from tqdm import tqdm

import config

# Define files path
audio_root = config.PATH_TO_RAW_AUDIO[config.DATA_DIR['MMAD']]  
text_root  = config.PATH_TO_TEXT_VECTORS[config.DATA_DIR['MMAD']]  
video_root = config.PATH_TO_RAW_VIDEO[config.DATA_DIR['MMAD']] 

def Generate_ComSeq(compseq, Alined_items):    
    for vid_key in tqdm(Alined_items, desc="Processing videos", unit="video"):
        intervals= []
        features= []
        compseq[vid_key]={} 
        file_path = os.path.join(video_root, f'{vid_key}.csv')
        with open( file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader) 
            for row in reader:
                row_np = np.array([  f'{float(val):.9e}' for val in row[3:]], dtype=np.float64)
                features.append(row_np)
                row_interval = np.array([ f'{float(row[2]):.9e}', f'{float(row[2])+ 0.04:.9e}'], dtype=np.float64)
                intervals.append(row_interval)
            # Convert the list of numpy arrays to a numpy array
            compseq[vid_key]["features"]= np.array(features)
            log.status("  <%s> computational sequence ...")
            #print(compseq[vid_key]["features"].shape)
            compseq[vid_key]["intervals"]=  np.array(intervals)
            #print(compseq[vid_key]["intervals"].shape)
 
if __name__=="__main__":

    #Initiate the visual comutational sequence
    CompSeq_OpenFace_Features={}
     
    #let's assume 
    Generate_ComSeq(CompSeq_OpenFace_Features,config.vid_keys)
    CompSeq_OpenFace=mmdatasdk.computational_sequence("MMAD_OpenFace")
    CompSeq_OpenFace.setData(CompSeq_OpenFace_Features,"MMAD_OpenFace")
    #NOTE: if you don't want to manually input the metdata, set it by creating a metdata key-value dictionary based on mmsdk/mmdatasdk/configurations/metadataconfigs.py
    CompSeq_OpenFace.deploy("MMAD_visual.csd")