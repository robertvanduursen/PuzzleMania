"""
11:53 - 14-01-2023
started in a frenzy
de midwinter pubcottage scene 3000 piece puzzle aan het einde van de zwangerschap


"""
'''
lol my artists friends webshopje

'''

# importing cv2
import cv2
import numpy as np

# path
path = r'/home/robert/Desktop/myWork/PuzzleMania/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg'
# Reading an image in default mode
image = cv2.imread(path)


def show_image(image):
    # Window name in which image is displayed
    window_name = 'image'

    # Using cv2.imshow() method
    # Displaying the image
    cv2.imshow(window_name, image)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()


# https://stackoverflow.com/questions/60772938/numpy-create-an-empty-alpha-image

def draw_puzzle_piece(image):
    # image = np.zeros((300, 300, 3), dtype=np.uint8)
    height = 300
    width = 300
    image_blank = np.zeros((height, width, 3), np.uint8)
    image_blank[:0:width] = (0, 255, 0)  # Green in BGR format

    return image_blank
    start_point = (5, 5)
    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = (220, 220)
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2
    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    # -1 thickness = filled
    image = cv2.rectangle(image, start_point, end_point, color, -1)

    start_point = (220, 100)
    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = (250, 150)
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2
    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    # -1 thickness = filled
    image_bit = cv2.rectangle(image, start_point, end_point, color, -1)

    # --------------------
    added_image = cv2.addWeighted(image, 0.4, image_bit, 0.1, 0)

    return added_image


def draw_puzzle_piece_2():
    height, width = 3, 4
    shape = (height, width)
    vector_value = (256, 256, 0)  # e.g. (red, green, blue)

    def create_new(shape, vector_value):
        image = np.empty((*shape, len(vector_value)))
        image[...] = vector_value
        return image

    image = create_new(shape, vector_value)
    return image


def draw_edge(image):
    # from __future__ import print_function
    import os
    # import imutils
    import cv2
    from PIL import Image
    import numpy as np

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # return gray
    thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)[1]
    # if imutils.is_cv2() or imutils.is_cv4():
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_NONE)
    # elif imutils.is_cv3():
    #     (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    #                                     cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(image, cnts, -1, (50, 50, 50), 24)

    RGBimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return RGBimage


H, W = 128, 256
blank_image = np.zeros((H, W, 4), np.uint8)

# Make first 10 rows red and opaque
blank_image[:10] = [255, 0, 0, 255]

# Make first 10 columns green and opaque
blank_image[:, :10] = [0, 255, 0, 255]
img = draw_edge(blank_image)

# img = draw_puzzle_piece_2()
show_image(img)
