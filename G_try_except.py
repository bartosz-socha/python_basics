# try

is_wrong = True

while is_wrong:
    try:
        num = int(input("Pass a number: "))
        print(num)
        is_wrong = False
    except ValueError as err:
        print(str(err) + " | Try again!")
    except:
        is_wrong = False

