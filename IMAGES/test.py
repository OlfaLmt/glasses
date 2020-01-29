# -*- coding: utf-8 -*-

import json
def information (num_img):
    with open ('ImageJSON.json') as json_data:
        a=json.load(json_data)
        i=str(num_img)
        x=a["data:img"+i]["regions"][0]["shape_attributes"]["all_points_x"]
        y=a["data:img"+i]["regions"][0]["shape_attributes"]["all_points_y"]
        list_info=[]
        list_info.append([x,y])
        print (list_info)
        
        

    
        