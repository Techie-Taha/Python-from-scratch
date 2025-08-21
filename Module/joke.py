# we installed pyjokes by typing pip install pyjokes in the terminal. just do import pyjokes
import pyjokes 
joke = pyjokes.get_joke() # get_joke(), a fixed function from the pyjokes module is called and its result is stored in the variable joke
print(joke)