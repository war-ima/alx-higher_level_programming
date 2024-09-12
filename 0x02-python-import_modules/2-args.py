#!/usr/bin/python3
def print_arg(argv):
    number = len(argv) - 1
    if number == 0:
        print("{:d} arguments.".format(number))
        return
    else:
        if number == 1:
            print("{:d} argument:".format(number))
        else:
            print("{:d} arguments:".format(number))
        t = 1
        while t <= number:
            print("{:d}: {:s}".format(t, argv[t]))
            t += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
