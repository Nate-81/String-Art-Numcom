from upload import *
import matplotlib.pyplot as plt
import numpy as np
import cv2

image_path = "/Users/nathans./Documents/NumCom/StringArt_Py/images/test.png"


def image_cleanup(img):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_img


def edge_points(img,n):
    edge_points = []
    height, width = img.shape
    # Define circle parameters (adjust these based on your image size)
    center_x = width // 2
    center_y = height // 2
    radius = min(center_x, center_y) - 1  # Ensure the circle is within the image bounds

    # Sample points along the circumference
    theta = np.linspace(0, 2 * np.pi, n)
    edge_points_x = np.uint16(center_x + radius * np.cos(theta))
    edge_points_y = np.uint16(center_y + radius * np.sin(theta))
    # edge_points.append((edge_points_x,edge_points_y))
    return edge_points_x, edge_points_y


if __name__ == '__main__':
    # run_app()
    image = cv2.imread(image_path)
    clean_image = image_cleanup(image)
    edge_x, edge_y = edge_points(clean_image,300)
    # cv2.imshow('Gray image', clean_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    plt.plot(edge_x,edge_y,'.')
    plt.show()
