#print evertything in list using for

beers = ['coors', 'miller', 'budweister', 'coronoa', 'amstel', 'guiness']
for beer in beers:
    print(beer.title())
print('I want a ', beer.title())  #this is outside the for loop indent, so it only executes once and "beer" is the last iteration, amstel

print('\n')
for beer in beers:
    print(beer.title())
    print('I want a ', beer.title())  #this is inside the for loop indent, so it executes everytime

print('\n')


#4.1 pizzas
pizzas = ['pizza hut', 'dominos', 'papa johns']
for pizza in pizzas:
    print(pizza)

print('\n')
for pizza in pizzas:
    print('I like',pizza.title(), 'pizza')
print('As you can see, I really like pizza. \nI guess I like',pizza.title(),'pizza the best.')

print('\n')


#Ranges

for value in range(1,6):
    print(value)

print('\n')
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11, 2))  #last number is by interval
print(even_numbers)


#print out squares using for loop
squares=[]
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#same as comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

print('\n')


#4-3
for value in range(1,21):
    print(value)

#4.4
print('\n')
'''for value in range(1,1000001):
    print(value) '''

#4.5
print(min(range(1,1000001)))
print(max(range(1,1000001)))
print(sum(range(1,1000001)))

#4.6
for odd in range(1,21,2):
    print(odd)

#4.7
for value in range(3,31,3):
    print(value)
print('\n')
#4.8
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

#4.9
cubes = [value**3 for value in range(1,11)]
print(cubes)
print('\n')



#4.10
print('The first three items in the beers list are', beers[:3])
print('The three beers in the middle are',beers[2:5])
print('The last three beers on my list are', beers[3:])

print('\n')


#4.11
your_beers = beers[:]
your_beers.append('colt 45')

print('My favorite beers are')
for beer in beers:
    print(beer.title())

print('\nYour favorite beers are')
for beer in your_beers:
    print(beer.title())
print('\n')


#4.13 TUPLES
print('Original food items are')
buffet =('eggs', 'bacon', 'pancakes', 'waffles', 'toast')
for food in buffet:
    print(food.title())

print('\nModified food items are')
buffet =('eggs', 'ham', 'grits', 'waffles', 'toast')
for food in buffet:
    print(food.title())
print('\n')
