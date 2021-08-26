greeting = "Good Morning, "
name = "Angela"

#Concatenating 
var = greeting + name
print(var)

#indexing
name = "Raju"
print(name[2])
print(name[0:3]) # -->0 include  also 1,2 no index 3 exclude
print(name[:3]) #is same as name [0:3]
print(name[1:]) #is same as name [1:3]

a = name[-3:-1] #same is name [2:3]
print(a)

#skip value of slicing
d = name[0:3:2]
print(d)

