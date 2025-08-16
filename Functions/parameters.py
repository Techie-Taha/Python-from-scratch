def user(name): #name in the parenthesis is the parameters
    print(f'Hi {name}')
    print("Welcome")
#if we try to run this program without calling the user(), in the terminal we won't see anything

user("Taha")
print("Now leave")

# we can print the same result, without using the parameters 
""" 
def user():
    name = "Taha"
    print(f'Hi {name}')
    print("Welcome")
user()
print("Now leave")
""" 
# we can also define multiple parameters 

def user(person_1,  person_2): #name in the parenthesis is the parameters
    print(f'Hi {person_1} and {person_2}')
    print("Welcome to the hotel")

#if we try to run this program without calling the user(), in the terminal we won't see anything

user("Taha","Nishat") #if I don't include person_2 we will get a error saying missing 1 required positional argument
print("Have a great time")