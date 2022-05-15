#display image
from IPython.display import display, Image
display(Image(filename='download.jpeg'))

#get image to matrix
import matplotlib.image as image
data=image.imread('download.jpeg')
print('The Shape of the image is:',data.shape)
print('The image as array is:')
print(data)

#matrix to image
from PIL import Image
import numpy as np
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
