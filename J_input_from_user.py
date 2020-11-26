# input

age = input("Enter your age: ")
print("You are old >> "+age)

var1 = float(input("first var: "))
calc = input("operator (+|-|/|*): ")
var2 = float(input("second var: "))


if calc == "+":
    print(var1 + var2)
elif(calc == "-"):
    print(var1 - var2)
elif(calc == "*"):
    print(var1 * var2)
elif(calc == "/"):
    print(var1 / var2)
else:
    print("Wrong operator")
