#opening a file
""" when accessing a file in directories...mostly windows make use of   back slashes..or double forward slashes"""

with open("C:\\Users\\Larry\\Documents\\index.txt") as file_object:
    contents = file_object.read()

print (contents)

#reading line by line
filename = "daily_zen.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line)
    

#storing the contents of a file in a list
with open(filename) as file_object:
    lists = file_object.readlines()

empty_lis=""
for line in lists:
    empty_lis += line.strip()
print (empty_lis)


#writing to a list
#empty file
filename = "weekly_zen.txt"
with open(filename ,'w') as file_object: # takes two arguments the filename , and the second tells py to open the file in write mode
    file_object.write("Welcome to the weekly zen of  py")




num1 = input("Enter the first number")
num2 = input("Enter the second number")
try:
    answer  = int(num1)/int(num2)
except ZeroDivisionError:
    print("you cant divide by zero")
else: 
    print(answer)


#file not found error
filename = "monthly_zen.txt"
try:
    with open(filename, 'a') as file_obj:
        file_obj.write("append this one ASAP")
except FileNotFoundError:
    print("The file wasnt found")

#working with multiple files
filenames = ['hello.txt', 'stoic.txt']

for file in filenames:
    try:
        with open(file, 'r') as file_object:
            full_text = file_object.read()
    except FileNotFoundError:
        print(f"filename {file} doesnt exist") #could use pass
    else:
        words = full_text.split()
        print(len(words))


