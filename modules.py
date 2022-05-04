#importing the wholemodule
import Functions
Functions.make_pizza("cheese","extra cheese")

#importing specific functions from a module
from Functions import make_pizza
make_pizza("cheese","vegies","mushrooms")

#importing all functions
from Functions import*
Functions.user_names("Henry")
