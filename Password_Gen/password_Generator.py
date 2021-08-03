#!/Python_Venv/env/bin/python
from struct import *
from random import random, seed
class Password_Gen:

    def __init__(self, length):
        self.lC = []
        self.uC = []
        self.symb = []
        self.dig = []
        self.length = length
        for i in range(0,10):
            self.dig.append(str(i))
        for i in range(65, 91):
            self.uC.append(chr(i))
        for i in range(97,123):
            self.lC.append(chr(i))
        for i in range(32, 48):
            self.symb.append(chr(i))
        for i in range(58, 65):
            self.symb.append(chr(i))
        for i in range(91, 97):
            self.symb.append(chr(i))
        for i in range(123, 127):
            self.symb.append(chr(i))
        self.total = len(self.lC) + len(self.uC) + len(self.symb) + len(self.dig)

    def lower_case(self):
        password = ""
        for i in range(self.length):
            password += self.lC[int(random() * len(self.lC))]
        self.display("All lower case:\n\n" + password)
    def upper_case(self):
        password = ""
        for i in range(self.length):
            password += self.uC[int(random() * len(self.uC))]
        self.display("All upper case: \n\n" + password) 
    def upper_and_lower(self):
        password = ""
        mash = self.lC + self.uC
        for i in range(self.length):
            password += mash[int(random() * len(mash))]
        self.display("Upper and lower case: \n\n" + password)
    def letters_and_numbers(self):
        password = ""
        mash = self.lC + self.uC + self.dig
        for i in range(self.length):
            password += mash[int(random() * len(mash))]
        self.display("Letters and numbers: \n\n" + password)
    def letters_special(self):
        password = ""
        mash = self.lC + self.uC + self.symb
        mashLen = len(self.lC) + len(self.uC) + len(self.symb) 
        for i in range(self.length):
            password += mash[int(random() * mashLen)]
        self.display("Letters and Special Characters:\n\n" + password)
    def grand(self):
        password = ""
        grand = self.lC + self.uC + self.symb + self.dig
        for i in range(self.length):
            password += grand[int(random() * self.total)]
        self.display("Mixture of Letters, Numbers, and Special Characters:\n\n" + password)
    def display(self, item):   
        print("-----------------\n")
        print(item)
        print("\n-----------------\n")
pass_len = input("How many characters do you want you password to be? \n")
test = Password_Gen(int(pass_len))
test.lower_case()
test.upper_case()
test.upper_and_lower()
test.letters_and_numbers()
test.letters_special()
test.grand()
