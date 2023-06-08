# *_*coding:utf-8 *_*
import os
 
 
DATA_DIR = {
	'MMAD': '/home/belgats/dataset/',
	'MMAD_V2': 'your data path',
}
PATH_TO_RAW_AUDIO = {
	'MMAD': os.path.join(DATA_DIR['MMAD'], 'opensmile'),
}
PATH_TO_RAW_VIDEO = {
	'MMAD': os.path.join(DATA_DIR['MMAD'], 'openface'),
}
PATH_TO_RAW_ANNOATION= {
	'MMAD': os.path.join(DATA_DIR['MMAD'], 'annotaion'),
}
PATH_TO_TEXT_VECTORS = {
	'MMAD': os.path.join(DATA_DIR['MMAD'], 'GLOVE'),
}
PATH_TO_LABEL = {
	'MMAD': os.path.join(DATA_DIR['MMAD'], 'labels'),
}
vid_keys=["1","2","3","4","5","6","7","8","9","10","11", "12","13","14",  "15",  "16",  "17",  "18",  "19",  "20","21", "22",  "23",  "24",  "25",  "26",  "27",  "28",  "29",  "30","31", "32",  "33",  "34",  "35",  "36",  "37",  "38",  "39",  "40"]
 
SAVED_ROOT = os.path.join('./saved')
DATA_DIR = os.path.join(SAVED_ROOT, 'data')
 