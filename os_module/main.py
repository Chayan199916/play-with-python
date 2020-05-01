import os

# print(os.getcwd())
# print(__file__)

class Demo:
    def __init__(self, name):
        self.name = name
        all_files = os.listdir('\\'.join(__file__.split('\\')[:-1]))
        for file in all_files:
            print(os.path.abspath(file))
    def show(self):
        print(self.name)