# lists

a_list = ["Kevin",99,"Kuba",1,0,True,"Klapek"]
b_list = ["Kevin",99,"Kuba",1,0,True,"Klapek"]
print(len(a_list))
print(a_list)
print(a_list[3:7])
print(a_list[6])
a_list[6] = "PAPA"
print(a_list[6])

a_list.extend(a_list) #rozszerz o inna liste
print(a_list)
a_list.append("MacOS") #dodaj na koncu
print(a_list)
a_list.insert(7, False) #dodaj w kontretnym miejscu
print(a_list)
a_list.remove("Kuba") #usun konkretny
print(a_list)
b_list.clear() #wyczysc całą liste
print(b_list)
a_list.pop() #usun ostatni element
print(a_list)
print(a_list.index("Kuba")) #wskaz index
print(a_list.count("Kevin")) #policz konkretny element
#a_list.sort() #sortowanie, nie dziala gdy list jest mieszana
a_list.reverse() #odwrócenie kolejności listy
c_list = a_list.copy() #wprowadzenie kopii listy do nowej listy

# 2D lists

new_list = [
    [1,2,3],
    ["dasd","rewrw","xcvxcv"],
    [True,False,True],
    [0]
]
new_list[2].insert(3,"nugat")

for row in new_list:
    for col in row:
        print(col)

# tuples

a_tuple = ("Kramp",3,12,False) #zbiorów typu 'tuple' nie można zmieniać
print(a_tuple[3])

# dictionaries

a_dict = {
    "Tres":3,
    "Quattro":4,
    5:"nuda"
}

print(a_dict[5])
print(a_dict.get("Tres","Not good!"))

