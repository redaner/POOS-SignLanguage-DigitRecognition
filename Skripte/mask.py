import numpy as np
import pandas as pd
import json
import warnings
from skimage.draw import polygon
from skimage import io
from indexOfSubstring import indexOfSubstring
import fileScripts as fs
import matplotlib.pyplot as plt
import os
from PIL import Image
from PIL import  ImageChops

warnings.filterwarnings('ignore')

def createMasks():

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

        fs.saveImage(mask[:, :, :], '/home/irhad/Desktop/POOS/Dataset/Masks/' + maskPath, 1, (0, 2))

def maskImages():
    maskPath = '/home/irhad/Desktop/POOS/Dataset/Masks/'
    originalImagePath = '/home/irhad/Desktop/POOS/Dataset/Images/'
    maskedImagePath = '/home/irhad/Desktop/POOS/Dataset/MaskedImages/'

    for i in range(0,10):
        for filename in os.listdir(originalImagePath + str(i)):
            #mask = io.imread(maskPath + str(i) + '/' + filename)
            #image = io.imread(originalImagePath + str(i) + '/' + filename)

            mask = Image.open(maskPath + str(i) + '/' + filename)
            image = Image.open(originalImagePath + str(i) + '/' + filename)
            image.load()
            mask.load()
            result = ImageChops.multiply(image,mask)
            result = np.asarray(result, dtype="int32")
            
            fs.saveImage(result[:, :, :], maskedImagePath + str(i) + '/' + filename)

            #plt.imshow(result)
            #plt.show()     

#createMasks()
maskImages()
    #plt.imshow(mask)
    #break
#plt.show()
