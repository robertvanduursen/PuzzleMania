import cv2
import numpy as np

height, width = 3, 4
shape = (height, width)
num_channels = 3
scalar_value = 0.5
vector_value = (256, 256, 0)  # e.g. (red, green, blue)

def create_new(shape, vector_value):
  image = np.empty((*shape, len(vector_value)))
  image[...] = vector_value
  return image

image = create_new(shape, vector_value)
cv2.imwrite('test.jpg', image)
