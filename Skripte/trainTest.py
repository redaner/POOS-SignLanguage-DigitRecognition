import os
from os import listdir
from os.path import isfile, join
import random
import numpy as np
from PIL import Image
import fileScripts as fs

dirname = os.path.dirname(__file__)

path_to_images = os.path.join(dirname, "../DataSet/MaskedImages")
path_to_results = os.path.join(dirname, "../DataSet/TrainTest")
images = []
os.makedirs(path_to_results + "/train")
os.makedirs(path_to_results + "/test") 

for i in range(0,10):
    images.append([f for f in listdir(path_to_images + "/" + str(i)) if isfile(join(path_to_images + "/" + str(i), f))])
    os.makedirs(path_to_results +"/train/" + str(i))
    os.makedirs(path_to_results+ "/test/" + str(i))
    
for i in range(0,10):
    images_for_class_i = images[i]
    length = len(images_for_class_i)
    first = random.randrange(0,length//2,5)
    second = random.randrange(length//2, length,6)
    for j in range(0, length):
        if j == first or j == second:
            fs.saveImage(np.asarray(Image.open(path_to_images + "/" + str(i) + "/" + images_for_class_i[j])), path_to_results + "/test/" + str(i) + "/" + images_for_class_i[j])
        else:
            fs.saveImage(np.asarray(Image.open(path_to_images + "/" + str(i) + "/" + images_for_class_i[j])), path_to_results + "/train/" + str(i) + "/" + images_for_class_i[j])