import glob
import requests
import json
import urllib.request

def getjson(filenames):
    # print(filenames)
    data = ''
    for file in filenames:
        url = "http://localhost:3000/api/json/%2F"+ file
        data = urllib.request.urlopen(url).read().decode()
        obj = json.loads(data)
        output = '/Users/divyachandana/Documents/NJIT/work/output/'
        # print(data)
        with open(output+file.replace(".jpg",".json"), 'w') as f:
            json.dump(obj, f, indent = 4)


filenames = glob.glob('*.jpg')
getjson(filenames)