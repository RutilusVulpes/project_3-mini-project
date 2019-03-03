import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
I1 = plt.imread('waldo_1.jpg')
I1 = I1.mean(axis=2)
plt.imshow(I1,cmap=plt.cm.gray)
plt.show()
