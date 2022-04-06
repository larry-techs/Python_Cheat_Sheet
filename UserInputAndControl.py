# to request for user input use input()
message = input("Enter the message ")

print (message)


age = input ("Enter your age")
age = int(age)
print(age)

#Restaurant boooking
Number_of_people = input("How many people are their?")
Number_of_people = int(Number_of_people)

if (Number_of_people >8):
    print("Sorry you will have to book another table")
else:
    print("Table available")



# While loops 
prompt = "\n welcome type anything:"
prompt +="\n type quit to exit"
message =  ''
while message != 'quit':
    message =input(prompt)
    if message != 'quit':
        print(message)

#using a flag 
active = True
while active:
    print("You still have health")
    health = input("Enter your health")
    health = int(health)
    if health<10:
        active = False

#Taking control of the loops 
# BREAK & CONTINUE

users = {}
user = 'jaimoh'
for v in users.values():
    while v != 'jaimoh':
        print("Balance added")
        if v == 'jaimoh':
            break
        
        
