#3.1
friends =['ponder', 'rzo','rufus']
print(friends[0].title())

print(friends[1].title())

print(friends[2].title())

#3.2
print('\nHey buddeh buddeh. How you doing, ',friends[0].title(),'?')

#3.3
vehicles=['GS 1200A', 'Hyundai Tiburon']
print('\nI will ride to Alaska on a ',vehicles[0])

#3.5
friends[1]='Timmy'
print(friends)

print(friends[-1],' cant make it.')
friends[-1]='Abdou'
print(friends[-1], 'will go instead')

#3.6
friends.insert(0, 'Rufus')
friends.insert(2,'Dufus')
print(friends)
friends.append('Jackamo')
print(friends)

#3.7
'''use pop() to remove guests one at a time until only two remain. each time i pop a name, print message saying i cant invite them
del last two names
print list
'''
friends.pop()
print('\n',friends)

len(friends)

friends.pop()
print('\n',friends)

friends.pop()
print('\n',friends)

friends.pop()
print('\n',friends)

friends.pop()
print('\n',friends)










'''
#p50  3-8


'''

#create list of locations
locations =['paris', 'london', 'tokyo', 'laguna seca', 'prudhoe bay']

#print third item
print('Third item is ',locations[2].title())

#print original
print('\nfull list is ',locations)

#print alpha sorted list on new line
print('\ntemporary alpha sorted list is ',sorted(locations))

#print original
print('\nfull list is ',locations)

#print list in reverse new line
print('\ntemporary reverse alpha list is', sorted(locations, reverse=True))
#print original
print('\nfull list is ',locations)

#print list sorted in reverse alpha
#locations.sort(reverse=True)
#print('reverse alpha is ',locations)


#reverse list
locations.reverse()
print('\npermanent reverse list is ',locations)


#reverse it again
locations.reverse()
print('\nback to original ', locations)


#permanent alpha sort
locations.sort()
print('\nlist permanantly alpha sorted', locations)

#permanent alpha reverse sort
locations.sort(reverse=True)
print('\nlist permanently reverse alpha sorted ',locations)

#print everything in list using for loop
print('\nThis is my list:')
for location in locations:
    print(location.title())

    