users = [""]

if users:
    for user in users:
        user = user.upper()
        if  "ADMIN" in user:
            print("welcome admin")
        else:
            print(f"welcome mr {user}")
    
else: 
    print("we need sime users")
            