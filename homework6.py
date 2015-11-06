__author__ = 'Michael Nowakowski and Joshua Shi'


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


def gerrymander(a, b):

    print len(a), len(b)
    print a[3], b[3]
    p = 0
    q = 0
    length_a = len(a)
    diff_array = [0 for x in range(length_a)]

    for i in range(len(a)):
        print a[i]-b[i]
        diff_array[i] = (a[i]-b[i])

    print diff_array
    for item in diff_array:
        if item >= 0:
            p += item
        else:
            q += item

    overall_sum = p-q
    neg_offset = abs(q)

    memo = [[[[0 for x in range(length_a)] for x in range(overall_sum)] for x in range(overall_sum)]
            for x in range(length_a)]
    #
    # for i in range(length_a):
    #     for j in range (length)
    return
