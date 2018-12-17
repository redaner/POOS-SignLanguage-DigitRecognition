from skimage import io

def saveImage(image, location):  
    io.imsave(location, image)