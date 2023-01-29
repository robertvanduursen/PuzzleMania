import cv2


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


