#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        imax = my_list[0]
        for n in my_list:
            if n > imax:
                imax = n
        return imax
    return None
