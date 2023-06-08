 
import mmsdk
from mmsdk import mmdatasdk
import numpy as np
import os
import csv
import json
  
import config
from tqdm import tqdm


# Define files path
audio_root = config.PATH_TO_RAW_AUDIO[config.DATA_DIR['MMAD']]  
text_root  = config.PATH_TO_TEXT_VECTORS[config.DATA_DIR['MMAD']]  
video_root = config.PATH_TO_RAW_VIDEO[config.DATA_DIR['MMAD']] 
annotation_root = config.PATH_TO_RAW_ANNOATION[config.DATA_DIR['MMAD']] 


def Generate_ComSeq(compseq, vid_keys): 
    for i, vid_key in tqdm(enumerate(vid_keys), total=len(vid_keys)):
        intervals= []
        features= []
        compseq[vid_key]={} 
        file_path = os.path.join(annotation_root, f'{vid_key}.json')
        with open(file_path ) as f:
            data = f.read()
            segments = {}
            points = {}
            line1 = data.split('\n')[0]
            line2 = data.split('\n')[1]           
            if line1: 
                obj1 = json.loads(line1)
                for segment_id in obj1:
                    st =  obj1[segment_id]['startTime']
                    et =  obj1[segment_id]['endTime']
                    row_np = np.array([ f'{float(st):.9e}',  f'{float(et):.9e}'], dtype=np.float64)
                    intervals.append(row_np)
                compseq[vid_key]["intervals"]= np.array(intervals)
            print( compseq[vid_key]["intervals"].shape)
            if line2:
                obj2 = json.loads(line2)
                for point_id in obj2:
                    if obj2[point_id]['labelText'] in ['-3', '-2', '-1', '0', '1', '2', '3']:
                        label = obj2[point_id]['labelText']
                        if float(label) < -1:
                            label = -1
                        if float(label) > 1:
                            label = 1        
                        print(label)
                        words_np = np.array([f'{float(label):.9e}'], dtype=np.float64)
                        features.append(words_np)
                compseq[vid_key]["features"]=  np.array(features)
            print( compseq[vid_key]["intervals"].shape)
 
 

if __name__=="__main__":

    compseq_labels_data={}
  
    #let's Arabic Multimodal 
    Generate_ComSeq(compseq_labels_data,config.vid_keys)
    compseq_Labels=mmdatasdk.computational_sequence("Labels")
    compseq_Labels.setData(compseq_labels_data,"Labels")
    #NOTE: if you don't want to manually input the metdata, set it by creating a metdata key-value dictionary based on mmsdk/mmdatasdk/configurations/metadataconfigs.py
    compseq_Labels.deploy("MMAD_Labels.csd")