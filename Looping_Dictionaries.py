users = []

users_1 = {'Name': "Eric",'Age':30,'level':"Hard"}
users_2 = {'Name':"Josh",'Age':28,'Level':"Medium"}

users = [users_1,users_2]

#Creating a fleet of enemies

enemy = []

for x in range(50):
    users_ = {'Name': "Eric",'Age':30,'level':"Hard"}
    enemy.append(users_)


#creating a list in a dictionary
pizza = {
    'topping':['Caramel','crust'],
    'Size':['Medium','Large']
}
print(pizza)


#dictionary in a dictionary
# Web users

users = {
    'Alalberto':{'FirstName':"Albert",'SecondName':"Einstein",'Age':34},
    'Granula':{'FirstName':"Granula",'SecondName':"Alnula",'Age':35}
}
for k , v in users.items():
    print(f"username is {k}")
    print(f"{v['FirstName']} {v['SecondName']}")
