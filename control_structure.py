## if statements
"""
Syntax

if condition:
    logic
else:
    logic
"""
## A program that accepts a number from the user

print("welcome to number Teller")
number= int(input("please enter a number between 1 and 9"))
if number ==1:
    print("you have entered number one")
elif number ==2:
    print("you have entered number two")
elif number ==3:
    print("you have entered number three")
elif number ==4:
    print("you have entered number four")
elif number ==5:
    print("print you have entered number five")
elif number ==6:
    print("print you have entered number 6")
elif number ==7:
    print("you have entered number 7")
elif number ==8:
    print("you have entered number 8")
elif number ==9:
    print("you have entered number 9")
else:
    print("invalid, please enter a number between 1 and 9")

#TODO
""
with the use of if statements, write a python program that allows an instructor to enter a mark strictly between 0 and 100

on recieving the mark, the program has to assign a grade based on your defined clusters ie 80-90 is A, 91-100 is A+ etc.
print("welcome to grading scale")
if marks >=91 and marks <=100:
    print("A+")
elif marks >=81 and marks <=90:
    print("A")
elif marks >=71 and marks <=80:
    print("B+")
elif marks >=61 and maks <=70:
    print("B")
elif marks >=51 and marks <=60:
    print("C+")
elif marks >=41 and marks <=50:
    print("C")
elif marks >=31 and marks <=40:
    print("D+")
elif marks >=21 and marks <=30:
    print("D")
elif marks >=10 and marks <=20:
    print("E")
elif marks >=0 and marks <=10:
    print("fail")

