from scipy import misc
from scipy import ndimage
import glob
import fileScripts as fs

for i in range(0,10):
    for filename in glob.glob("C:\\Users\\user\\Desktop\\POOS-SignLanguage-DigitRecognition\\Dataset\\Images\\" + str(i) + "\\*.JPG"):
        image = misc.imread(filename)
        filteredImage  = ndimage.median_filter(image, 1)

        split = filename.split('\\')

        fs.saveImage(filteredImage, "C:/Users/user/Desktop/POOS-SignLanguage-DigitRecognition/Dataset/DenoisedImages/" + str(i) + "/" + split[len(split) - 1])
