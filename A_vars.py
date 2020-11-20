# vars

p_name = "MYSKu"
p_age = 43
p_number = 180
p_bool = False

try:
    print("Hi " + p_name)
    print(p_name + " is good")
    print("Everything about " + p_name + " is good")
    print(p_name + " is " + str(p_age) + " yare alt")
except TypeError as t_err:
    print("!!" + str(t_err) + "!!")