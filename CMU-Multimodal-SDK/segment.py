import json
import os

nb_segment = 0
nb_segmentp = 0
nb_segmentn = 0
total_time = 0

for file_name in os.listdir('/home/slasher/Downloads/dataset/V2/annotation/'):
    if file_name.endswith('.json'):
        with open('/home/slasher/Downloads/dataset/V2/annotation/'+file_name) as f:
            data = f.read()
            segments = {}
            points = {}
            line1 = data.split('\n')[0]
            line2 = data.split('\n')[1]
            sgemnt_time = 0
            if line1: 
                obj1 = json.loads(line1)
                for segment_id in obj1:
                    if obj1[segment_id]['startTime'] <= 1 :
                        nb_segment = nb_segment+1
                    nb_segment = nb_segment+1
                    segments[segment_id] = {'startTime': obj1[segment_id]['startTime'],
                                        'endTime': obj1[segment_id]['endTime']}
                    a = obj1[segment_id]['endTime']-  obj1[segment_id]['startTime']
                    sgemnt_time = sgemnt_time +  a
                total_time = total_time+  sgemnt_time
                #print(sgemnt_time)
            if line2:
                obj2 = json.loads(line2)
                for point_id in obj2:
                    if obj2[point_id]['labelText'] in ['-3', '-2', '-1', '0', '1', '2', '3']:
                        if obj2[point_id]['labelText']  in ['3', '2'] :
                            nb_segmentn = nb_segmentn+1
                        if obj2[point_id]['labelText'] in [ '0'] :
                            nb_segmentp = nb_segmentp+1
                        print(obj2[point_id]['labelText'])
                        points[point_id] = {'labelText': obj2[ point_id]['labelText'],
                                    'segment_id': obj2[point_id ]['segment_id']}
                        segments[segment_id]['labelText'] = obj2[point_id]['labelText']
print(total_time)
print(total_time/500)