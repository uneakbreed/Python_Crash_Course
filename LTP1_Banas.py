#https://www.youtube.com/watch?v=nwjAHQERL08

name = input('What is your name?\n')
print("How's it hanging,",name+"?")

print()
#Ask the user to input 2 values and store them in variables num1 num2
num1, num2 = input('Gimme two numbers, fool!\n---->').split()

#convert the strings into regular numbers
num1 = int(num1)
num2 = int(num2)

#add the values entered and store is sum
sum = num1 + num2

#subtract values and store in difference
difference = num1 - num2

#multiply values an dstore in product
product = num1 * num2

#divide values and store in quotient
quotient = num1 / num2

#use modulus on the values to find the remainder
remainder = num1 % num2

#print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
print('That was the long way, created variable for each calculation \n'
      'then printed each separately')
#another way of doing all of that from lines 8-34
print()
num1, num2 = input('Gimme two more, buddeh\n---->').split()

#convert the strings into regular numbers
num1 = int(num1)
num2 = int(num2)

import operator
ops= {"+":operator.add, "-":operator.sub, '*':operator.mul, '/':operator.truediv, "//":operator.floordiv}
for symbol in ops:
    print("{} {} {} = {}".format(num1, symbol,num2, ops[symbol](num1,num2)))
print('That was the SHORT way, created dictionary of operators \n'
      'then ran a for loop to print each calculation')


#Problem: recieve miles and convert to kilometers
print()
miles= input("Gimme miles, I'll convert to kilometers")
miles = int(miles)
#kilometrs = miles * 1.60934
convert = miles * 1.60934
#Enter Miles 5

#5 miles equals 8.04
print("{} miles is {} kilometers".format(miles, convert))




#Enter calcuation: 5 * 6
#5 * 6 = 30

#Store the user input of two numbers and the operator of choice
num1, symbol, num2 = input('Gimme a calculation biatch').split()


#if they enter + then we need to provide output based on addition
if symbol == '+':
    print(num1,' + ',num2,' = ', num1+num2)
elif symbol == '-':
    print(num1,' - ',num2,' = ', num1-num2)
elif symbol == '*':
    print(num1,' * ',num2,' = ', num1*num2)
elif symbol == '/':
    print(num1,' / ',num2,' = ', num1/num2)
elif symbol == '**':
    print(num1,' ** ',num2,' = ', num1**num2)
elif symbol == '//':
    print(num1,' // ',num2,' = ', num1//num2)
elif symbol == '%':
    print(num1,' % ',num2,' = ', num1%num2)
else: print("Use either + - / % ** //")
print('That was the long way, using elif staments to determine operator used \n'
      'then nested each calculation print statemnt')



#Store the user input of two numbers and the operator of choice
print()
num1, symbol, num2 = input('Gimme a another calculation kid').split()

#convert the strings into integers
num1 = int(num1)
num2 = int(num2)

#another way is to import the operator then create a dictionary. not working
import operator
ops ={'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '%':operator.mod, '//':operator.floordiv, '**':operator.xor}
print(str(num1)+' '+symbol+' '+str(num2),'=',ops[symbol](num1,num2))
print('This is the short way, create dictionary of operators, \n'
      'call correct operator value based on user key input')


# We'll provide different outputs based on age

#1 - 18 --> Important
#21,50, > 65 --> Important
#All others--> no one cares about you!!!


#Receive age and store in age
age = eval(input('Enter age: '))
#if age is both >= 1 and <= 18 Important
age = int(age)
if age>=1 and age <= 18:
    print('You special')
elif age==21 or age ==50 or not(age<65):
    print('You special')
#if age is either 21 or 50 important

#if age less than 65 then convert true to false and vice versa
else: print('Seriously, who gives AF about you???!')
#not important


#If age is 5 Go to Kindergarten

#If age is 6 - 17 then goes to grades 1 -12

#if age is greater than 17 say go to college

#Try to complete with 10 or less lines

age = int(input('Soooo, how old are you???'))
if age == 5:
    print('Are ya ready kids???!')
elif age >=6 and age <=17:
    print('sounds like you belong in grades 1-12')
elif age >= 17:
    print('House party 2?')
else: print("You don't get to go to school, ya loser!")