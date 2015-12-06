__author__ = 'Michael Nowakowski and Joshua Shi'

import numpy

def reading_weeping(day_array, section_array):
    print day_array
    print section_array

    # memo = [[]
    return


def string_interleaving(a, b, c):
    """
    :param a: string of characters (ex. "XY")
    :param b: string of characters (ex. "ST")
    :param c: an interleaved string of characters in order from a and b (ex. "XSYT")
    :return: Boolean value, is c an interleaving of strings a and b?
    """
    print 'A = ', a, "B = ", b, 'C = ', c
    length_a = len(a)
    length_b = len(b)
    length_c = len(c)

    if len(a) is 0 and len(b) is 0 and len(c) is 0:
        return True

    memo = [[0 for x in range(length_b+1)] for x in range(length_a+1)]

    for i in range(length_a+1):
        for j in range(length_b+1):

            # both a and b are empty!
            if (i is 0) and (j is 0):
                memo[i][j] = True
                print "case 1"
                print memo

            # a is an empty string, and B = C
            elif (i is 0) and (c[j-1] == b[j-1]):
                memo[i][j] = memo[i][j-1]
                print "case 2"
                print memo

            # b is an empty string, and A = C
            elif (j == 0) and (c[i-1] == a[i-1]):
                print "case 3"
                print memo
                memo[i][j] = memo[i-1][j]

            # if a is equal, but not b
            elif (a[i-1] == c[i+j-1]) and (b[j-1] is not c[i+j-1]):
                memo[i][j] = memo[i-1][j]
                print "case 4"
                print memo

            # if b is equal, but not a
            elif (a[i-1] != c[i+j-1]) and (b[j-1] == c[i+j-1]):
                memo[i][j] = memo[i][j-1]
                print "case 5"
                print memo

            # if c is equal to both a and b
            elif (a[i-1] == c[i+j-1]) and (b[j-1] == c[i+j-1]):
                memo[i][j] = (memo[i-1][j] or memo[i][j-1])
                print "case 6"
                print memo

    return memo[length_a][length_b]


def gerrymander(u_list):

    length_u = len(u_list)
    print length_u
    n = length_u
    half_size = (length_u)/2
    print "n = ", n, "half_size = ", half_size
    maxiumum_value = 0
    minimum_value = 0
    diff_array = [0 for x in range(length_u)]

    for i in range(length_u):
        print u_list[i][0]-u_list[i][1]
        diff_array[i] = (u_list[i][0]-u_list[i][1])

    print diff_array
    for item in diff_array:
        if item >= 0:
            maxiumum_value += item
        else:
            minimum_value += item

    print "max = ", maxiumum_value, "min = ", minimum_value
    overall_sum = maxiumum_value-minimum_value
    neg_offset = abs(minimum_value)
    new_max = maxiumum_value+neg_offset

    print "neg offset = ", neg_offset
    for i in range(len(diff_array)):
        diff_array[i] = diff_array[i]+neg_offset

    memo = numpy.zeros(shape=(length_u, half_size, new_max, new_max))
    # memo = [[[[0 for x in range(length_u)] for x in range(half_size)] for x in range(neg_offset)] for x in range(new_max)]
    for p in range(new_max):
        for q in range(new_max):
            if p > neg_offset and q > neg_offset:
                memo[0][0][p][q] = True

    for i in range(1, length_u):
        for k in range(1, half_size):
            for p in range(neg_offset-1):
                for q in range(new_max-1):
                    # print i, k, p, q
                    # if i == 0 or k == 0:
                    #     pass
                    # else:
                    memo[i][k][p][q] = memo[i-1][k-1][p-diff_array[i]][q] or memo[i-1][k][p][q-diff_array[i]]

    for p in range(new_max):
        for q in range(new_max):
            if memo[length_u-1][half_size-1][p][q]:
                print True
                return True

    return False

