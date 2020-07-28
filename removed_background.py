import cv2
import numpy as np
import os

"""
   Basic idea is to take the bitwise And of image with mask generated
   for green colored pixels values ranges.
   The non zero pixels of the image when multiplied with 1
   values of the mask will get 1 and
   green pixels are since 0 in the mask so all green
   pixels when multipled by 0 will become 0
   eventually replacing green with black now hence
   we get a green background free image.
"""


def read_image(filename, files):
    if filename not in files:
        raise Exception("Image does not exist")
    try:
        filepath = "images/" + image_name
        image = cv2.imread(filepath)
    except:
        print("Error occurred try again")
    return image


def show_files():
    print("Images in the images folder")
    files = os.listdir("images/")
    for i in files:
        print(i)
    print("-" * 20)
    return files


def remove_background(image, path):
    try:
        cv2.imshow("Original Image", image)
        cv2.waitKey(0)
        # convert the image to RGB
        HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # To create mask set the lower and upper pixel
        # range of mask using HSV values
        # HSV Value ranges for green color
        lower_green = np.array([25, 52, 72])
        upper_green = np.array([102, 255, 255])
        # create mask of image using lower and upper range of
        # pixels values for RGB
        mask = cv2.inRange(HSV_image, lower_green, upper_green)
        # Take not of mask to swap 0 with 1 and vice versa
        # so that green region pixels become 0
        mask = ~ mask
        cv2.imshow("Mask", mask)
        cv2.waitKey(0)
        # in this mask which is a binary image consisting of only 1 and 0.
        # green pixels are 0 and all other pixels are 1
        output = cv2.bitwise_and(image, image, mask=mask)
        cv2.imshow("Output Image", output)
        cv2.waitKey(0)
        cv2.imwrite(path, output)
        print("Image saved in path", path)
    except:
        print("Error occurred try again")
    return


# Show list of images in the images folder
files = show_files()
# Take image name as input
print("Enter filename from any of the above images")
image_name = input()
print("-" * 20)
image = read_image(image_name, files)
# Set path for output file
path = "removed/" + "removed_" + image_name
remove_background(image, path)
