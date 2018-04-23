# https://www.youtube.com/watch?v=swQEbZ6ez1I
for i in [2,4,6,8,10]:
    print("i = ", i)
print()
for i in range(2,11,2):
    print("i = ", i)
print()
for i in range(2,11):
    if i%2 == 0:
        print('i = ',i)


print()
for j in range(10):
    print("j = ", j)


print()
for k in range(3,10):
    print("k = ", k)

#even number using modulus i % 2 == 0


print()
#print odds from 1 - 20
for i in range(1,21,2):
    print(i)

print()
for i in range(1,21):
    if ((i% 2) != 0):
        print(i)

print()
your_float = input("Enter a float: ")
your_float = float(your_float)
print("Round to 2 decimals : {:.2f}".format(your_float))


#Have the user enter their investment amount and epected intterest
#Each year their investment will increase by their investment + interest rate
#Print out the earnings after a 10 year period
print()
inv= input("How much you putting in?")
inv = float(inv)
ret= input('Whats your rate of return?')
ret = float(ret)
ret= float(ret)*.01

for i in range(10):
    inv= inv+(inv*ret)
    print('At year:', i+1,', the toal amount is:{:.2f}'.format(inv))
print()
print('Your return after 10 years is: {:.2f}'.format(inv))


#while loop
print()
import random
rand_num =random.randrange(1,51)

i = 1
while (i != rand_num):
    i += 1
print("The random value is : ", rand_num)

print()
i = 1
while i <=20:
    if(i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("odd :", i)
    i +=1


#problem:
# How tall is the tree: 5
    #
   ###
  #####
 #######
    #

#Use 1 while loop and 3 for loops
#4 spaces : 1 hash
#3 spaces: 3 hashes
#2 spaces: 5 hashes
#1 space: 7 hashes
#0 spades: 9 hashes

#Need to do
#1. decrement spaces by 1 each time trough the loop
#2. increment the hashes by 2 each time through loop
#3. save spaces to the stump by calculating tree height - 1
#4. decrement from tree height until it equals 0
#5. Print spaces and then hashes for each row
#6. Print stump spaces and then 1 hash


#get the number of rows for the tree
tree_height = input('How tall is this tree? ')


#convert into an integer
tree_height = int(tree_height)

#get the starting spaces for the top of the tree
spaces = tree_height - 1

#there is one hash to start that will be incremented
hashes = 1

#save stump spaces til later
stump_spaces = tree_height - 1

#make sure the right number of rows are printed
while tree_height != 0:

#print spaces
    for i in range(spaces):
        print(' ', end="")

#print hashes
    for i in range(hashes):
        print("#", end="")

#newline after each row is printed
    print()
#that spaces is decremented by 1 each time
    spaces -=1
#hashes incremented by 2 each time
    hashes +=2
#decrement tree height to jump out of loop
    tree_height -= 1

#print the spaces before the stump and then the hash
for i in range(stump_spaces):
    print(' ', end="")
print('#')