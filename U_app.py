# 1 1 2 3 5 8 13 21 34 55 89 144

def mysk_fibbo1(end_of_string):
    old = [0]
    new = [1]
    for string in range(1, end_of_string):
        old.append(new[string - 1])
        new.append(new[string - 1] + old[string - 1])
    new.insert(0, 0)
    return new



def mysk_fibbo2(end_of_string):
    old = [0]
    new = [1]
    string = 1
    is_done = False
    while not is_done:
        old.append(new[string - 1])
        new.append(new[string - 1] + old[string - 1])
        string += 1
        if new[string - 1] + old[string - 1] > end_of_string:
            is_done = True
    new.insert(0, 0)
    return new


print(mysk_fibbo1(10))
print(mysk_fibbo2(10))

from L_classes import *

obj1 = MyStudy("Bartosz", 28, 4.7)
obj2 = MyStudy("Miłosz", 22, 4.2)
obj3 = MyStudy("Kalosz", 19, 3.2)
obj4 = MyStud("Lucjusz", 5, 3.1)

print(obj1.is_old())
print(obj4.name)
obj4.is_dumb()
print(obj4.name)







### guessing game
"""
secret_word = "shoe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and out_of_guesses == False:
    guess = input("Guess a word: ")
    guess_count += 1
    if guess_count == guess_limit:
        out_of_guesses = True

if out_of_guesses == True:
    print("You lose")
else:
    print("You win! It's a "+ secret_word)
"""

### translator
'''
def my_translator(word):
    trans = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.islower():
                trans = trans + "x"
            else:
                trans = trans + "X"
        else:
            trans = trans + letter
    return trans

print(my_translator(input("Pass a word: ")))

#word = input("Pass a word to translate: ")
'''
### desktop app
"""
import tkinter as tk
window=tk.Tk()
window.title(" My Calculator ")
window.geometry("600x400")
butt = tk.Button(text="Press me!!")
butt.grid(column=7,row=7)
window.mainloop()
"""
