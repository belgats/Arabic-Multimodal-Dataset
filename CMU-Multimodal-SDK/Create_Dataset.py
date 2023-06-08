#word_level_align.py
#first aligns a dataset to the words vectors and collapses other modalities (by taking average of them for the duration of the word). After this operation every modality will have the same frequency (same as word vectors). Then the code aligns based on opinion labels (note that collapse does not happen for this step.

import mmsdk
from mmsdk import mmdatasdk
import numpy
import dataset_folds

import pickle
import config

#uncomment all the ==> lines together

#A simple averaging technique. More advanced methods can be built based on intervals.
def myavg(intervals,features):
        return numpy.average(features,axis=0)


#Downloading the dataset
ammd_hightlevel=mmdatasdk.mmdataset(dataset_folds.highlevel,'MMAD/')
#cmumosi_highlevel=mmdatasdk.mmdataset('cmumosi/')

#some random video from cmumosi_highlevel
#==>some_video=list(cmumosi_highlevel["glove_vectors"].data.keys())[0]

#The next line is not needed for standard datasets as they are all sorted based on intervals in computational sequence entries
#cmumosi_highlevel.sort()

#Aligning to the words to get word-level alignments
ammd_hightlevel.align('bert_vectors',collapse_functions=[myavg])
#ammd_hightlevel.impute('bert_vectors')
#print(cmumosi_highlevel["OpenFace"].data)

#get the intervals and features accompanying the 100th word in the some_video
#==>some_video_100th_word=some_video+'[100]'
#==>for compseq_name in list(cmumosi_highlevel.computational_sequences.keys()):
#==>	compseq=cmumosi_highlevel[compseq_name]
#==>	print (compseq_name)
#==>	print (numpy.array(compseq.data[some_video_100th_word]["intervals"]).shape,numpy.array(compseq.data[some_video_100th_word]["features"]).shape)
#==>	print ("-------")


#Aligning to the computational labels, thus removing the unsupervised components of CMU-MOSI

ammd_hightlevel.add_computational_sequences(dataset_folds.labels,'MMAD/')
ammd_hightlevel.align('Opinion Segment Labels')
ammd_hightlevel.hard_unify()

#get the intervals and features accompanying the 2nd in some_video
#==>some_video_2nd_segment=some_video+'[2]'
#==>for compseq_name in list(cmumosi_highlevel.computational_sequences.keys()):
#==>	compseq=cmumosi_highlevel[compseq_name]
#==>	print (compseq_name)
#==>	print (numpy.array(compseq.data[some_video_2nd_segment]["intervals"]).shape,numpy.array(compseq.data[some_video_2nd_segment]["features"]).shape)
#==>	print ("-------")

#Deploying the files to the disk and reading them again - Building machine learning models start right after this. No need to do alignment multiple times since aligned files can be deployed and used again.
deploy_files={x:x for x in ammd_hightlevel.computational_sequences.keys()}
ammd_hightlevel.deploy("./deployed",deploy_files)
#Reading the dumped file can be as easy as just calling the mmdataset on the deployed folder
aligned_ammd_hightlevel=mmdatasdk.mmdataset('./deployed')
#Now let's get the tensor ready for ML - right here we just get everything into ML ready tensors. But you should split the aligned_cmumosi_highlevel based on the standard CMU MOSI folds
#get the standard folds using mmsdk.mmdatasdk.cmu_mosi.standard_folds.standard_x_fold for x={train,test,valid}

tensors=ammd_hightlevel.get_tensors(seq_len=25,non_sequences=["Opinion Segment Labels"],direction=False,folds=[dataset_folds.standard_train_fold, dataset_folds.standard_valid_fold,dataset_folds.standard_test_fold])

fold_names=["train","valid","test"]

 
# Load text data from HDFS
# Construct the dataset dictionary
dataset  = {'train': {'text': None, 'audio': None, 'vision': None, 'labels': None},
                'valid': {'text': None, 'audio': None, 'vision': None, 'labels': None},
                'test': {'text': None, 'audio': None, 'vision': None, 'labels': None}}
# Populate the dataset with the data
dataset['train']['text'] = tensors[0]["bert_vectors"]  # Set test text data
dataset['train']['audio'] = tensors[0]["OpenSMILE"] # Set test audio data
dataset['train']['vision'] = tensors[0]["OpenFace" ] # Set test vision data
dataset['train']['labels'] = tensors[0]["Opinion Segment Labels"]  # Set test label data
dataset['valid']['text'] = tensors[1]["bert_vectors"]  # Set test text data
dataset['valid']['audio'] = tensors[1]["OpenSMILE"] # Set test audio data
dataset['valid']['vision'] = tensors[1]["OpenFace" ] # Set test vision data
dataset['valid']['labels'] = tensors[1]["Opinion Segment Labels"]  # Set test label data
dataset['test']['text'] = tensors[2]["bert_vectors"]  # Set test text data
dataset['test']['audio'] = tensors[2]["OpenSMILE"] # Set test audio data
dataset['test']['vision'] = tensors[2]["OpenFace" ] # Set test vision data
dataset['test']['labels'] = tensors[2]["Opinion Segment Labels"]  # Set test label data
 
with open('MMAD.pkl', 'wb') as f:
	pickle.dump(dataset, f)

















