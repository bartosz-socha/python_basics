class MyStudy:

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def is_old(self):
        if self.age >= 25:
            a = True
        else:
            a = False
        return a

    def is_good_student(self):
        if self.gpa <= 4.5:
            a = False
        else:
            a = True
        return a


class MySt:

    def is_mine(self):
        print("echo")


class MyStud(MyStudy, MySt):

    def is_dumb(self):
        self.name = "You are douchebag"


c = MyStudy("Bart", 24, 3.2)
print(c.is_old())

g = MyStudy("Kalosz", 12, 4)
