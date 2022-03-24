#check if new username is in current users

current_users = ["jane"]
new_user=["Jane","john"]
for user in new_user:
    user = user.upper()
    for current in current_users:
        current = current.upper()

        if user in current:
            print(f"{user } oops already taken")
        else: 
            print(f"{user } username available")

#this will capitalize the whole list
print(current_users)
for i in range(len(current_users)):
    print(i)
    current_users[i] = current_users[i].upper()
    print (current_users)