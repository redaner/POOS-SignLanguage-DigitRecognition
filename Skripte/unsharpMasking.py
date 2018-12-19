from scipy import misc
import cv2
import glob
import fileScripts as fs
import skimage
import numpy

for i in range(0,10):
    for filename in glob.glob("C:\\Users\\user\\Desktop\\POOS-SignLanguage-DigitRecognition\\Dataset\\DenoisedImages\\" + str(i) + "\\*.JPG"):
        image = misc.imread(filename)
        
        lap = cv2.Laplacian(image, cv2.CV_64F)
        
        
        sharpImage = image - 0.1*lap
        sharpImage = sharpImage.astype(numpy.uint8)
        

        split = filename.split('\\')

        fs.saveImage(sharpImage, "C:/Users/user/Desktop/POOS-SignLanguage-DigitRecognition/Dataset/UnsharpMaskedImages/" + str(i) + "/" + split[len(split) - 1])
