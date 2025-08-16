#data = {}, this is an empty dictionary, but in the curly braces we can define multiple unique key values following by a comma
data = {
    "name": "Taha Ahmed",
    "age": 21,
    "is_verified": True
    # we are allowed to add strings, integers, boolean like everything but has to be unique.

}
#data["name"] = "Max" , we can also update the information
data["birth date"] = "July 10th, 2004" #can add more info outside of the curly braces like this 
print(data["name"])
print(f'Birth date: {data["birth date"]}')