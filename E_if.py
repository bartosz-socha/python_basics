# if

var3 = 11

is_good = False

if var3 > 20 and var3 <= 22 and not(is_good):
    print("CASE 1")
elif var3 < 10 or var3 > 99 and var3 < 199:
    print("CASE 2")
elif var3 == 200 and var3 != 199:
    print("CASE 3")
else:
    print("CASE X")