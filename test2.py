import sys

def main():

    if len(sys.argv) > 1:
        input_argument = "Isay/" + sys.argv[1]
        print(input_argument)
    else:
        print("no")


main()