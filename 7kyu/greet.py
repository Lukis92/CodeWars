# https://www.codewars.com/kata/5121303128ef4b495f000001/train/python

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)