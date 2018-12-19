from PIL import ImageEnhance
from PIL import Image
import glob
import numpy
import fileScripts as fs

for i in range(0, 10):
    for filename in glob.glob("C:\\Users\\user\\Desktop\\POOS-SignLanguage-DigitRecognition\\Dataset\\DenoisedImages\\" + str(i) + "\\*.JPG"):
        
        image = Image.open(filename)
        
        enhancer = ImageEnhance.Contrast(image)
        
        enhanced = enhancer.enhance(2)
        
        split = filename.split('\\')
        
        fs.saveImage(numpy.asarray(enhanced, dtype="uint8"), "C:/Users/user/Desktop/POOS-SignLanguage-DigitRecognition/Dataset/IncreasedContrast/" + str(i) + "/" + split[len(split) - 1])
        
        