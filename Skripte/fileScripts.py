from skimage import io
import numpy as np

def saveImage(image, location, rot, flip):  
    io.imsave(location, np.flip(np.rot90(image, rot), flip))
    #np.rot90(image, 3)

def saveImage(image, location):  
    io.imsave(location, image)
    #np.rot90(image, 3)