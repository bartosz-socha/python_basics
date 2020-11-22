#print("Hello, Python Basics!")
#print(0)
#echo


def make_sand(a: int):
    try:
        if type(a) is int:
            print(a)
        else:
            raise TypeError
    except TypeError as run:
        print(str(run) + "| Variable is not int |")

#dasd
#make_sand(1)


var1 = input("Enter a number: ")
var2 = input("Enter a number: ")

print("First: " + str(var1) + ", Second: " + str(var2))

print("First: {}, Second: {}".format(var1, var2))

