# if syntax
x,y,z= 10,11,12
if (x<y) and (y<z):
    print("you qualify")
# The in check on list

group_users = ["Henry", "Vedi","idev","carlk"]
user = "diego"

if user in group_users:
    print(f"{user} exists in the group")

# The not check 
if user not in group_users:
    print(f"{user} doesnt exist")

alien_color = ["green","yellow","red"]
alien_shot = "red"
if alien_shot=="green":
    points = 5
elif alien_shot == "red":
    points = 10
else:
    points ="0"

print(points)
words = "hello", "me"
words = list(words)




#Checking if a list is empty

students =[]
if students:
    print("empty students")
else:
    print("not empty")

#Checking between two lists

students_ = ["jimmy","jaimoh","hnery","henry"]
students_fail = ["jimmy","jaimoh","larry"]

for student in students_:
    if student in students_fail:
        print(f"{student}you have failed!!")
    else:
        print (f"{student}you made it")
    

