
# coding=utf-8
#! /usr/bin/python
import sys
import json
import csv
import io
import pandas as pd
import numpy as np

LOCATION_TEMP_FOLDER = 'temps'
class ServiceUtils():
    def __init__(self):
        print("ServiceUtils")
    def writeFileDataJSON(self,data_filter, file_name):
        print("escribiendo archivo")
        FILE_LOCATION_ALL = ("%s/%s.json" % (LOCATION_TEMP_FOLDER,file_name))
        with open(FILE_LOCATION_ALL, 'w') as filehandle:  
            filehandle.write('[\n')
            count = 0
            for listitem in data_filter:
                if count < len(data_filter)-1:
                    filehandle.write('%s,\n' % listitem)
                    
                else:
                    filehandle.write('%s\n' % listitem)
                count +=1
            filehandle.write('\n]')
    def writeFileJSON(self,data,file_name):
        print("escribiendo archivo")
        FILE_LOCATION_ALL = ("%s/%s.json" % (LOCATION_TEMP_FOLDER,file_name))
        with open(FILE_LOCATION_ALL, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def openJSONFile(self,file_name):
        print("abriendo archivo")
        FILE_LOCATION_ALL = ("%s/%s.json" % (LOCATION_TEMP_FOLDER,file_name))
        with open(FILE_LOCATION_ALL) as f:
            data_load = json.load(f)
            return data_load
    def writeCSV(self,data,file_name):
        np.savetxt(file_name, data, delimiter =", ", fmt ='% s')
    def saveDataFrame(self,dataFrame,file_name):
        df = pd.DataFrame(dataFrame)
        df.to_csv()
