
#get the intervals and features accompanying the 100th word in the some_video
#==>some_video_100th_word=some_video+'[100]'
#==>for compseq_name in list(cmumosi_highlevel.computational_sequences.keys()):
#==>	compseq=cmumosi_highlevel[compseq_name]
#==>	print (compseq_name)
#==>	print (numpy.array(compseq.data[some_video_100th_word]["intervals"]).shape,numpy.array(compseq.data[some_video_100th_word]["features"]).shape)
#==>	print ("-------")


#Aligning to the computational labels, thus removing the unsupervised components of CMU-MOSI

cmumosi_highlevel.add_computational_sequences(dataset.labels,'cmumosi/')
cmumosi_highlevel.align('Opinion Segment Labels')
cmumosi_highlevel.hard_unify()

#get the intervals and features accompanying the 2nd in some_video
#==>some_video_2nd_segment=some_video+'[2]'
#==>for compseq_name in list(cmumosi_highlevel.computational_sequences.keys()):
#==>	compseq=cmumosi_highlevel[compseq_name]
#==>	print (compseq_name)
#==>	print (numpy.array(compseq.data[some_video_2nd_segment]["intervals"]).shape,numpy.array(compseq.data[some_video_2nd_segment]["features"]).shape)
#==>	print ("-------")

#Deploying the files to the disk and reading them again - Building machine learning models start right after this. No need to do alignment multiple times since aligned files can be deployed and used again.
deploy_files={x:x for x in cmumosi_highlevel.computational_sequences.keys()}
cmumosi_highlevel.deploy("./deployed",deploy_files)
#Reading the dumped file can be as easy as just calling the mmdataset on the deployed folder
aligned_cmumosi_highlevel=mmdatasdk.mmdataset('./deployed')
#Now let's get the tensor ready for ML - right here we just get everything into ML ready tensors. But you should split the aligned_cmumosi_highlevel based on the standard CMU MOSI folds
#get the standard folds using mmsdk.mmdatasdk.cmu_mosi.standard_folds.standard_x_fold for x={train,test,valid}

tensors=cmumosi_highlevel.get_tensors(seq_len=25,non_sequences=["Opinion Segment Labels"],direction=False,folds=[dataset.standard_train_fold, dataset.standard_valid_fold,dataset.standard_test_fold])

fold_names=["train","valid","test"]

for i in range(3):
	for csd in list(cmumosi_highlevel.keys()):
		print ("Shape of the %s computational sequence for %s fold is %s"%(csd,fold_names[i],tensors[i][csd].shape))

