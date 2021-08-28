# english to bangla translate

myDict = {
    "pankha" : "Fan",
    "ghori" : "Watch",
    "kedara" : "chair"
}
print("Option are : ",myDict.keys())
a = input("Enter the Bangla Word\n")
# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:",myDict.get(a))

# display unique number

num1 =int(input("Enter the number 1\n"))
num2 =int(input("Enter the number 2\n"))
num3 =int(input("Enter the number 3\n"))
num4 =int(input("Enter the number 4\n"))
num5 =int(input("Enter the number 5\n"))
num6 =int(input("Enter the number 6\n"))
num7 =int(input("Enter the number 7\n"))
num8 =int(input("Enter the number 8\n"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)

# find the length
s = {20, 20.0, "20"}
print(s)
print(len(s))

# favourite language select as unique

favLang = {}
a = input("Enter Your Language Shoum\n")
b = input("Enter Your Language Karishma\n")
c = input("Enter Your Language Jammy\n")
favLang["Shoum"] = a
favLang["Karishma"] = b
favLang["Jammy"] = c
print(favLang)
