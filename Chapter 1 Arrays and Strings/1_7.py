# Problem 1.7

# Write an algorithm such that if
# an element in an MxN matrix is 0, its entire row and column is set to 0.

# BigO(<2N)

def make_it_zero(matrix):
    """
    :type matrix: array
    """

    # Dimensions of the matrix
    m = image.__len__()
    n = image[0].__len__()

    print 'Shape ', m, ' x ', n

    ind_zero_elements = []
    row_ind = -1

    # Finding Indices of Zero elements
    for element in matrix:
        row_ind += 1
        col_ind = -1

        row = element[:]

        for x in row:
            col_ind += 1
            if x == 0:
                ind_zero_elements.append([row_ind, col_ind])

    for index in ind_zero_elements:
        print index
        # Making Rows Zeros
        for x in range(n):
            p = index[0]
            q = x
            image[p][q]= 0

        # Making Column Zeros
        for y in range(m):
            p = y
            q = index[1]
            image[p][q] = 0

    print image
    return image

image = [[0, 1, 4, 1], [2, 3, 1, 0], [4, 1, 1, 1]]
print image

make_it_zero(image)
