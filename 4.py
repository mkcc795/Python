class Student:
    def __init__(self, name=None, heinght = 160):
        self.name = name
        self.heinght = heinght
    def __bool__(self):
        return self.name != None
    def __len__(self):
        retorn f"яка довжина в нас зріст = {self.heinght}"
    def __del__(self):
        print("11111")
nick = Student()
print(nick.__bool__())
print(nick.__len__())
print(len(nick))
print(bool(nick))
