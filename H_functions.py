# functions

def echo(text):
    print(text)


# echo("Pysku, Pysku")

def say_mysk(name, age):
    new = age + 5
    #print("Hello " + name + "! You're " + str(new))


# say_mysk("Pysk", 25)

def batman(var1, var2, var5):
    wynik = var1 * (var2 + var5)
    return wynik


var3 = batman(2, 1, 99)
#print(var3)


def my_power(base, powe):
    resu = base
    for uno in range(powe - 1):
        resu = resu * base
    return resu


#print(my_power(2, 11))

#print(pow(2, 11))
