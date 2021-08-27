letter = ''' Dear |<NAME>|,
 You are Selected for my company.
Date: |<DATE>|
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("|<NAME>|",name)
letter = letter.replace("|<DATE>|",date)
print(letter)

#Detect double space
string = "This is a string with double  spaces"
doubleSpaces = string.find("  ")
# doubleSpaces = string.replace("  "," ")
print(doubleSpaces)
print(string)

#formating letter
letter = "Dear Sam, Python is very interesting! Thanks!"
print(letter)
format_letter = "Dear Sam,\n\tPython is very interesting!\nThanks!"
print(format_letter)