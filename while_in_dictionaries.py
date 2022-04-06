#bad code 
active_users = ['nel','len','kin','nik']
inactive_users= ['nel','len']

while inactive_users:
    for inactive_user in inactive_users:

        for active_user in active_users:
            if (inactive_user == active_user):
                active_users.remove(inactive_user)
                inactive_users.remove(inactive_user)
                
print("hello")
print(active_users)


#confirming new users to a website
new_users = ['Henry',"john"]
users =[]
while new_users:
    new_user = new_users.pop()
    print(f"{new_user} is the new user")

    users.append(new_user)

print(users)