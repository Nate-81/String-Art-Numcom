from upload import *
import matplotlib.pyplot as plt
import numpy as np
import cv2

image_path = "/Users/nathans./Documents/NumCom/StringArt_Py/images/test.png"


def image_cleanup(img):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_img


if __name__ == '__main__':
    # run_app()
    image = cv2.imread(image_path)
    clean_image = image_cleanup(image)
    # cv2.imshow('Gray image', clean_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(clean_image)
