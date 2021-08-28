# Declare the set
a = {1, 2, 3, 4}
print(a)

a ={} #its return as dictionary

# creating an empty set
b = set()
print(type(b))

# Adding value to the empty set
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4,5,6)) #we can add tuple because it hash valut
b.add({3:2}) # cannot add list or dictionary to sets
print(b)

print(len(b)) # prints the length of this set

b.remove(5) #remove 15
b.remove(15) # throws an error because its not present in the set
print(b)

print(b.pop()) # remove random value from set
print(b)