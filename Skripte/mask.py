import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import os

x_l = np.load(os.path.join(os.path.dirname(__file__), 'X.npy'))
Y_l = np.load(os.path.join(os.path.dirname(__file__), 'Y.npy'))
img_size = 64
plt.subplot(1, 2, 1)
plt.imshow(x_l[260].reshape(img_size, img_size))
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(x_l[900].reshape(img_size, img_size))
plt.axis('off')

plt.show()

#def maskImage(originalPath, maskPath):