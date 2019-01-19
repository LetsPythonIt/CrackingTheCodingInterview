# Problem 1.6

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes
# write a method to rotate the image by 90 degrees.

# Implementation using extra space.

import numpy as np

layer_array = []  # Our Global container


def rotate_image(image):
    # @image: where image is a nxn matrix of pixel values

    print 'Received Image: \n', image

    # What's the size of our image?
    (n, m) = image.shape

    # Rotated Image Container - image_buffer
    image_buffer = np.zeros([n, m], dtype=np.int)

    for row in range(n):
        for column in range(m):
            image_buffer[m - column - 1][row] = image[row][column]
    print 'Rotated Image: \n', image_buffer

    return image_buffer


# Test cases
image = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
Array = rotate_image(image)
