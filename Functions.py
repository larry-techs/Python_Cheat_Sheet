#normal defination
def welcome():
    print("Hey thier , welcome back")

welcome()
#defination with keyword parameter

def welcome(user_name,user_id):
    print(f"welcome , {user_name}\n")
    print ("Your id is", user_id)


welcome(user_id=7586893,user_name= "henry")

#Calling a function with an optional value
def user_names(first_name , last_name , middle_name = ""):
    """optional value should be initialized as empty"""
    if middle_name:
        formarted_names = f"welcome ,{first_name} {middle_name} {last_name}"
    else:
        formarted_names = f"welcome , {first_name} {last_name}"
    
    return formarted_names

print(user_names("henry", "ray","harry"))
print(user_names("henry","harry"))


#music dictionary in a function

def make_album(album_name,album_artist,number_of_songs = 0):
    album={'album_name': album_name,'album_artist':album_artist,'number_of_songs':number_of_songs}
    return album

while True:
    album_name = input("Emter the album name ,")
    if album_name == "q":
        break
    album_artist = input ("enter the album artist ,")
    if album_artist == "q":
        break

    album = make_album(album_name,album_artist)
    print(album)
#passing an arbitrary number of parameters    

def make_pizza(*topppings):
    print(f"making pizza with toppings , {topppings}")

make_pizza("cheese","pepperoni","vegies")

#list and functions
def greet_user(users):
    for user in users:
        print(f"hello{user}")

users = ['jerry','henry','john','harry','schrin']
greet_user(users[:]) #send a copy of the list to the function

