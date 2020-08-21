from helpers.strings import *
from helpers.strings import extract_lower
from helpers import variables

#print(f"__name__ in main.py: {__name__}")

print("Here" + __name__)

print(f"Lowercase letters: {extract_lower(variables.name)}")
print(f"Uppercase letters: {extract_upper(variables.name)}")