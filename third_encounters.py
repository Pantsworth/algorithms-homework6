__author__ = 'Michael Nowakowski and Joshua Shi'


def string_interleaving(a, b, c):
    """
    takes 3 strings and determines whether c is a valid interleaving of the letters of a and b
    strings a and b can be present an arbitrary number of times k1 and k2
    :param a: string
    :param b: string
    :param c: interleaved string
    :return:
    """
    length_a = len(a)
    length_b = len(b)
    length_c = len(c)

    print "strings: ", "a = ", a, "b = ", b, "c = ", c
    # print "lengths: ", length_a, length_b, length_c
    if length_c == 0:
        return False

    c = " " + c
    solution_number = 0
    memo = [False for x in range(len(c)+1)]

    for k in range(length_c+1):
        # print k
        if k == 0:
            memo[0] = [(-1, -1), (-1, -1)]

        elif (k > 0) and (memo[k-1] is not False):
            memo[k] = eval_solutions(memo[k-1], k-1, a, b, c)
            solution_number = max(len(memo[k]), len(memo[k-1]))
            # print memo[k]

    # print memo[length_c]
    if memo[length_c]:
        for sol in memo[length_c]:
            if (sol[0] == len(a)-1) and (sol[1] == len(b)-1):
                print True
                # print "SOLUTION NUMBER: ", solution_number
                return True
            else:
                pass
    print "FAILED"
    return False


def add_to_list(new_sol, sol_list):
    if new_sol not in sol_list:
        sol_list.append(new_sol)
    return sol_list


def eval_solutions(list_of_sol, c_pos, a, b, c):
    sol_list = []

    for sol in list_of_sol:
        # print sol

        # case: both are possible
        if (sol[0] < len(a)-1) and (sol[1] < len(b)-1):
            #append both options
            if a[sol[0]+1] == c[c_pos+1] and b[sol[1]+1] == c[c_pos+1]:
                # print "case 1: append both options"
                new_sol = (sol[0]+1,sol[1])
                sol_list = add_to_list(new_sol, sol_list)
                new_sol = (sol[0], sol[1]+1)
                sol_list = add_to_list(new_sol, sol_list)

            if b[sol[1]+1] == c[c_pos+1]:
                # print "case 2: append just b"
                new_sol = (sol[0], sol[1]+1)
                sol_list = add_to_list(new_sol, sol_list)

            if a[sol[0]+1] == c[c_pos+1]:
                # print "case 3: append just a"
                new_sol = (sol[0]+1, sol[1])
                sol_list = add_to_list(new_sol, sol_list)

        # wrap-around for a
        if (sol[0] == len(a)-1) and a[0] == c[c_pos+1]:
            # print "case 4: a returns to 0"
            new_sol = (0, sol[1])
            sol_list = add_to_list(new_sol, sol_list)

        # wrap-around for b
        if (sol[1] == len(b)-1) and (b[0] == c[c_pos+1]):
            # print "case 5: b returns to 0"
            new_sol = (sol[0], 0)
            sol_list = add_to_list(new_sol, sol_list)

        # see if a or b are possible:
        # if (sol[0] < len(a)-1) or (sol[1] < len(b)-1):
        if sol[0] < len(a)-1:
            if a[sol[0]+1] == c[c_pos+1]:
                # print "case 9: just a"
                new_sol = (sol[0]+1, sol[1])
                sol_list = add_to_list(new_sol, sol_list)

        if sol[1] < len(b)-1:
            if b[sol[1]+1] == c[c_pos+1]:
                # print "case 10: just b"
                new_sol = (sol[0], sol[1]+1)
                sol_list = add_to_list(new_sol, sol_list)

        else:
            pass

    if sol_list:
        # print "sol_list = ", sol_list
        return sol_list

    else:
        return False

string_interleaving("xxy", "xxz", "xxxxyzxxyxxzxxyxxxyxz")
string_interleaving("ab", "bc", "abbc")
string_interleaving("abba", "accava", "accabbavaa")
string_interleaving("a", "b", "aaaab")
string_interleaving("xxxxxxxxxx","xxxxxxxxxx",("xxxxxxxxxxxxxxx"+"xxxxxxxxxxxxxxx"))
