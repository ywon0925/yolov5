import os
import json


dir_path = os.getcwd()
json_list = os.listdir(dir_path + '/origin_ann')
json_list.remove('.DS_Store')
i = 1
for json_file in json_list:
    print(i)
    # read original json
    with open(dir_path + '/origin_ann/' + json_file) as f:
        anns = json.load(f)
    ann_dict = {"objects": []}

    # convert to wanted shape in python dict
    for ann in anns['Annotations']:
        bbox_dict = {'classTitle':'',
                     'points':{
                         'exterior': [],
                         'interior': []
                     }}
        
        if ann['classname'] not in ['hood', 'turban','hijab_niqab']:
            # save class name
            if ann['classname'] == 'mask_colorful' or ann['classname'] == 'mask_surgical':
                bbox_dict['classTitle'] = 'mask'
            elif ann['classname'] == 'face_other_covering':
                bbox_dict['classTitle'] = 'face_no_mask'
            elif ann['classname'] == 'eyeglasses':
                bbox_dict['classTitle'] = 'glasses'
            else:
                bbox_dict['classTitle'] = ann['classname']
                                   
            # save bounding box points
            bbox_points = ann['BoundingBox']
            bbox_dict['points']['exterior'].append([bbox_points[0] , bbox_points[1]])
            bbox_dict['points']['exterior'].append([bbox_points[2] , bbox_points[3]])
        
            ann_dict['objects'].append(bbox_dict)
        
    # write a new json file using the dict
    with open(dir_path + '/Medical Mask/ann/' + json_file, 'w') as jf:
        json.dump(ann_dict, jf)
    i += 1


