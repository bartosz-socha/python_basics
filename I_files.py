### files
# reading

#import csv as c
#b_file = open("w_file.txt", "r")
#if b_file.readable():
#    a_csv = c.reader(b_file,delimiter=":")
#    for dot in a_csv:
#        print(dot)
#b_file.close()

##READ
a_file = open("w_file.txt", "r")
if a_file.readable():
    a_list = a_file.readlines()
    print(a_list)
a_file.close()

##APPEND or WRITE
c_file = open("w_file.txt", "a")
c_file.write("mu:du:goo\n")
c_file.close()

##READ AGAIN
a_file = open("w_file.txt", "r")
if a_file.readable():
    a_list = a_file.readlines()
    print(a_list)
a_file.close()

# r - read file
# a - append or create new file
# w - overwrite or create new file
