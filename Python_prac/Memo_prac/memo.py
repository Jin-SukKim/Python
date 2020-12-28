import sys

# python memo.py -a "Life is too short."

#sys.argv[0] : memo.py
option = sys.argv[1] # -a (option : -a, -m, ect.)


if option == "-a":
    memo = sys.argv[2] # user input (string)
    with open("memo.txt", "a") as f:
        # print(memo, file = f) # same as f.write()
        f.write(memo)
        f.write("\n")
elif option == "-v":
    with open("memo.txt", "r") as f:
        print(f.read())


