#-------------Dictionary Practice------------------
dict1={"name":"Abdur Rehman","age":22 ,"city":"rahim yar khan"}
print(type(dict1)) #it will print <class 'dict'> because it is a dictionary
print(dict1)
print(dict1["age"])
#we can also use get method to access the value of a key
dict1["city"]="lahore"
print(dict1)
print(len(dict1)) 

#--------add new key-value pair in dictionary----------------
dict1["country"]= "Pakistan"
print(dict1)
print(len(dict1))

#--------remove key-value pair from dictionary----------------
del dict1["country"]
print(dict1)

print(dict1.values())
print(dict1.keys())

#-------update value of a key in dictionary----------------
dict1.update({"age": 23})
print(dict1)

