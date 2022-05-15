#display image
from IPython.display import display, Image
display(Image(filename='download.jpeg'))

#get image to matrix
import matplotlib.image as image
data=image.imread('download.jpeg')
print('The Shape of the image is:',data.shape)
print('The image as array is:')
print(data)

#image data dimensions, get value
data.shape 
data[][][]

#matrix to image
from PIL import Image
import numpy as np
img = Image.fromarray(data, 'RGB')
img.save('my_image.png')
img.show()

#define matrix, vector
x = tf.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
y = tf.constant([[1.],[2.],[3.]])

#multiplication
z = tf.matmul(x, y)

#sudo pip3 install sk-video
#sudo apt-get install ffmpeg

#video to matrix
import skvideo.io  
videodata = skvideo.io.vread("my_video.mp4")  
print(videodata.shape)

# frame/height/width/RGB
videodata[][][][]
