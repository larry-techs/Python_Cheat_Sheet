#declaration in dictionaries
alien_0= {} # an empty dictionary
alien_0 = {'color':'green' , 'points': 5}

print(alien_0['color'])
print (alien_0['points'])

#adding values to dictionaries
alien_0['position_X'] = 25
alien_0['position_Y'] = 25
print(alien_0)

#to remove an element from dictionary use keyword del
del alien_0['points']

weapons_damage = {}
weapons_damage ['gkl'] = 80
weapons_damage['Lpg'] = 45
print(weapons_damage)

#using get() to access Values
Mgk_damage = weapons_damage.get('Mgk', 'no Mgk damage assigned')
print(Mgk_damage)

#iterating through a dictionary 
aliens = {'toshu':'color','hoku':'yello','Giru':'pink','Rama':'red'}

new_aliens =["shang","hioku","ratu","Giru"]

for alien in aliens.keys():
    print("\n",alien)

    if  alien in new_aliens:
        print(f"{alien}, already exists")
    elif "shoru" not in aliens.keys:  # error 
        aliens['shoru'] = "green"

print (aliens)

#to find the values in  a dictionary use method values()
for value in aliens.values():
    print(value)
#to print only the unique values use method set()
for values in set(aliens.values()):
    print (values)




