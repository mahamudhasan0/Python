myDict = {
    "fast" : "In a Quick Manner",
    "mahamud" : "A coder",
    "marks" : [1,2,5],
    "anotherDict" : {'mahamud' : 'Player'},
    1 : 2
}

# Dictionary Methods
print(list(myDict.keys())) #prints the keys of dictionary
print(myDict.values()) #prints the values of the dictionary
print(myDict.items()) #prints the (key,value) for all contents of the dictionary
print(myDict)
updateDict = {
    "friend" : "jammy",
    "car" : "allion",
    "mahamud" : "A dancer"
}
myDict.update(updateDict) #update the dictionary by adding key-values pairs from updateDict
print(myDict)

print(myDict.get("fast")) #prints value associated with key "fast"
print(myDict["fast"])

# The difference between .get and [] syntax is dictionaries
print(myDict.get("fast2")) # Returns None as fast2 is not present in the dictionary
print(myDict["fast2"]) #throws an error as fast2 is not present in the dictionary