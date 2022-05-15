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

#read and save audio file
from scipy.io.wavfile import write
import audio2numpy as a2n
x,sr=a2n.audio_from_file("file.mp3")
write("example.wav", sr, x)

#pip install audio2numpy

#create sine wave
from scipy.io.wavfile import write
samplerate = 44100; fs = 100
t = np.linspace(0., 1., samplerate)
amplitude = np.iinfo(np.int16).max
data = amplitude * np.sin(2. * np.pi * fs * t)
write("example.wav", samplerate, data.astype(np.int16))
