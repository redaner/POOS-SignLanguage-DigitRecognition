import numpy as np
import pandas as pd
import json
import warnings
from skimage.draw import polygon
from indexOfSubstring import indexOfSubstring
import fileScripts as fs

warnings.filterwarnings('ignore')

regionsOfInterestJSON = open('/home/irhad/Desktop/POOS/Dataset/RegionsOfInterest/Sign-L.json')
annotationStrings = regionsOfInterestJSON.readlines()

for jsonString in annotationStrings:
    jsonData = json.loads(jsonString)
    maskPath = indexOfSubstring(jsonData['content'], 'IMG')

    mask = np.zeros([100,100,3], dtype=int)
    points = jsonData['annotation'][0]['points']
    poly = []
    for point in points:
        poly.append((int(point[0] * 100), int(point[1] * 100)))
    poly = np.array(poly)
    rr, cc = polygon(poly[:,0], poly[:,1], mask.shape)
    mask[rr,cc,:] = (255, 255, 255)

    fs.saveImage(mask[:, :, :], '/home/irhad/Desktop/POOS/Dataset/Masks/' + maskPath)

    #plt.imshow(mask)
    #break
#plt.show()
#def maskImage(originalPath, maskPath):