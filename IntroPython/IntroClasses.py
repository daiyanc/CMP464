# https://dropbox.com/work/CMP464788Fall2021_DataHandlingAndAnalysis


class Person:
    def __init__(self, name, age):  # This is the constructor, keyword is init
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name + " | " + str(self.age))


me = Person("Daiyan", 21)
me.print_info()
