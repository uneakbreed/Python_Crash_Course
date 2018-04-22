#6.1
lauren = {'sex': 'female', 'height':66, 'weight': 160, 'height_incr':'inches', 'weight_incr':'lbs', 'occupation':'bartender'}
print('Lauren is a',lauren['sex'])

#6.3
print()
glossary = {'del': 'delete', 'if': 'if else', 'elif': 'if else if'}
print(glossary)

print()
for key in glossary.keys():
    print(key)

print()
for value in glossary.values():
    print(value)

#can i print the dictionary key AND the value in a for in statement??
print()
for key, value in glossary.items():
    print(key+': means',value)


#6.6
print()
candidates = ['jen', 'JB', 'edward', 'abdou',  'sarah']
favorite_languages = {
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',

}
for candidate in candidates:
    if candidate in favorite_languages:
        print('Thanks for taking the poll,',candidate.title(),'your favorite language is',favorite_languages[candidate].title()+'.')
    else:
        print("C'mon,", candidate.title(),'take the poll, son!')


#Make an empty list for storing aliens
print()
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'speed':'slow', 'points':5}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created
print('Total number of aliens:', str(len(aliens)))



#Make an empty list for storing aliens
print()
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'speed':'slow', 'points':5}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color'] == 'yellow'
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')