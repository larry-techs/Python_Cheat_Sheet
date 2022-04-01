users = {}
users['Name'] = 'player1'
users['Age'] = 25
users['Mode'] = 'easy'
users['Name']=users['Name'].upper()
print (users)

for k,v in users.items():
    print (f"key : {k}")
    print(f"value: {v}")