import cv2
import numpy as np

# path
path = r'/home/robert/Desktop/myWork/PuzzleMania/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg'
# Reading an image in default mode
image = cv2.imread(path)

if __name__ == '__main__':
    from show_image import show_image

    show_image(image)
