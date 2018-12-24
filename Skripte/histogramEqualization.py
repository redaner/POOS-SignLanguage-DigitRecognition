import numpy as np
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
import fileScripts as fs

dirname = os.path.dirname(__file__)

path_to_images = os.path.join(dirname, "../Dataset/Images")
path_to_results = os.path.join(dirname, "../Dataset/HistogramEqualized")
images = []

for i in range(0,10):
    images.append([f for f in listdir(path_to_images + "/" + str(i)) if isfile(join(path_to_images + "/" + str(i), f))])
    if not os.path.isdir(path_to_results + "/" + str(i)):
        os.makedirs(path_to_results + "/" + str(i))
        
for i in range(0,10):
    length = len(images[i])
    for j in range(0, length):
        image = np.asarray(Image.open(path_to_images + "/" + str(i) + "/" + images[i][j]))
        hist, bins = np.histogram(image, 256, [0,256])
        
        cum_sum = hist.cumsum()
        cum_sum_masked = np.ma.masked_equal(cum_sum, 0) 
        cum_sum_masked = (cum_sum_masked - cum_sum_masked.min()) * 255 / (cum_sum_masked.max() - cum_sum_masked.min())
        cum_sum = np.ma.filled(cum_sum_masked,0).astype("uint32")
        
        image_modified = (np.uint8(cum_sum[image]))
        
        fs.saveImage(image_modified,path_to_results + "/" + str(i) + "/" + images[i][j])