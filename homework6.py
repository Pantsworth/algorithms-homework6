__author__ = 'Michael Nowakowski and Joshua Shi'


def reading_weeping(day_array, section_array):
    print day_array
    print section_array

    memo = [[]


    return


def first_encounters(a, b, c):
    print 'A = ', a, "B = ", b, 'C = ', c
    length_a = len(a)
    length_b = len(b)

    if len(a) is 0 and len(b) is 0 and len(c) is 0:
        return True

    memo = [[0 for x in range(length_a+1)] for x in range(length_b+1)]

    for i in range(length_a+1):
        for j in range(length_b+1):

            if (i is 0) and (j is 0):
                memo[i][j] = True
                print "case 1"
                print memo

            elif (i is 0) and (c[j-1] == b[j-1]):
                memo[i][j] = memo[i][j-1]
                print "case 2"
                print memo

            elif (j == 0) and (c[i-1] == a[i-1]):
                memo[i][j] = memo[i-1][j]
                print "i= ", i
                print "case 3"
                print memo

            elif (a[i-1] != c[i+j-1]) and (b[j-1] is not c[i+j-1]):
                memo[i][j] = memo[i-1][j]
                print "case 4"
                print memo

            elif (a[i-1] != c[i+j-1]) and (b[j-1] == c[i+j-1]):
                memo[i][j] = memo[i][j-1]
                print "case 5"
                print memo

            elif (a[i-1] == c[i+j-1]) and (b[j-1] == c[i+j-1]):
                memo[i][j] = (memo[i-1][j] or memo[i][j-1])
                print "case 6"
                print memo

    print memo[length_a][length_b]
    return memo[length_a][length_b]


def gerrymander(a, b):

    diff_array = []
    p = 0
    q = 0
    length_a = len(a)

    for i in len(a):
        for j in len(b):
            diff_array[i] = (a[i]-b[j])

    for item in diff_array[i]:
        if item >= 0:
            p += item
        else:
            q += item

    overall_sum = p-q
    neg_offset = abs(q)

    memo = [[[[0 for x in range(length_a)] for x in range(overall_sum)] for x in range(overall_sum)] for x in range (length_a)]
    #
    # for i in range(length_a):
    #     for j in range (length)
    return
