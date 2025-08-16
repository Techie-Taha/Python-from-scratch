""""
name = "x"
age = 20
print(int(name) * 20)
"""
# when we run this program our system crashes with a ValueError, in order to avoid the crash out
try:
    age = 20
    name = "x"
    print(int(name) * 20)
except ValueError:
    print("Invalid action") #Now the program won't crash, instead in the terminal we will see Invalid action with a exit code 0