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


