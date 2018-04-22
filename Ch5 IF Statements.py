#5.4
alien_color = 'yellow'
if alien_color =='green':
    print('You earned 5 points!')
else:
    print('You earned 10 points!')

#5.5

if alien_color=='green':
    print('You earned 5 points!')
elif alien_color=='yellow':
   print('You earned 10 points!')
else:
    print('You earned 15 points!')
print('\n')

#5.6
age = input('Whats your age, boy-o!\n')
age = int(age)  #need to convert string to number. input is always stored as string
if age <2:
    print('Ya fuckin baby')
elif age <4:
    print('Oh ya little shit')
elif age <13:
    print('Snot nosed, brat')
elif age <20:
    print('Yeah yeah, no one understands you')
elif age <65:
    print('You aint no spring chicken no more')
else:
    print('Damn you old!')
print()

#5.7
beers = ['coors', 'miller', 'budweister', 'coronoa', 'amstel', 'guiness']
beer = 'Mad Dog 20/20'
if beer in beers:
    print('lets chug this bitch!')
else:
    print('I aint drinkin that piss water')
print()


#5.8
usernames = ['dadgums', 'lauren', 'Admin', 'codebreaker', 'slacker']
for username in usernames:
    if username =='Admin':
        print('Hello, Admin. Would you like to see a status report?')
    else:
        print('Hello,',username+'. Thank you for loggin in.')
print()

#5.9
usernames2 = []
if usernames2:
    for username in usernames2:
        if username =='Admin':
            print('Hello, Admin. Would you like to see a status report?')
        else:
            print('Hello,',username+'. Thank you for loggin in.')
else:
    print('Damn, we need some users! Seriously, WTF!')
print()


#5.10
current_users = usernames[:]
current_users_lower = [x.lower() for x in current_users]  #uses a comprehension to make all usernames in list lowercase for comparison
new_users = ['ponder', 'timmeh', 'admin', 'rufus', 'codebreaker']
new_users_lower = [x.lower() for x in new_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user+'? Nah dog, pick another username')
    else:
        print('Howdy,',new_user)

#5.10.1
new_user = input('Whats your username?\n')
if new_user.lower() in current_users_lower:
   print(new_user+'? Nah dog, you cant have it')
else:
        print('Howdy,',new_user)


'''
#5.10.2  create a while loop that continuously asks until a unique username is entered

new_user = input('Whats your username?\n')
if new_user in current_users:
   print(new_user+'? Nah dog, you cant have it)
else:
        print('Howdy,',new_user)
'''

#5.11
for ordinal in range(1,10):
    if ordinal==1:
        print("1st")
    elif ordinal ==2:
        print('2nd')
    elif ordinal ==3:
        print('3rd')
    else:
        print(str(ordinal)+'th')
