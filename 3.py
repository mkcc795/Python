class Student:
    def __init__(self):
        self.height = 170
    height = 160
    def printer(self):
        print(self.height)
    def change_high(self,new_height):
        self.height = new_height
niks = Student()
niks.printer()
niks.change_high(174)
niks.printer()
