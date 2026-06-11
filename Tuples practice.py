#--------------Tuples practice----------------
tuple1=("Sheikh","Hasan","Al-Mamun")
print(tuple1)
print(tuple1[0])
print(len(tuple1))
#------Nested tuple----------------
tuple2=(1,2,3,[4,5,6],7)
print(tuple2)
print(type(tuple2))
print(type(tuple2[3]))

#-------tuple can be defined by different ways----------------
tuple3=1,2,3,4,5 #without parenthesis
print(tuple3)   
print(type(tuple3))

t4=1.2
print(type(t4))
print(type((t4,))) #convert float to tuple

#------------single value Tuple-----------------
t5=(1,) #single value tuple
print(t5)
print(type(t5))

#------if......
t5=(1) #not a tuple
print(t5) #Because of single value without comma, it is not a tuple
print(type(t5)) #it is an integer, not a tuple

#-------indexing in tuple----------------
tuple4=(1,2,3,4,5)
print(tuple4[0]) #indexing starts from 0
print(tuple4[1])
print(tuple4[1:4]) #slicing
print(tuple4[1: ]) #when we write like this, it will print from index 1 to the end of the tuple
print(tuple4[ :4]) #when we write like this, it will print from the beginning of the tuple to index 3 (4 is not included)

#-------concatenation of tuples----------------
tuple5=(6,7,8)
tuple6=tuple4+tuple5
print(tuple6)

tuple7=("hey i am " ,)
tuple8=("a","tuple")
tuple10=tuple7+tuple8
print(tuple10)

#-------Min,Max,sum function in tuple----------------
tuple9=(6,2,9,4,5)
print("Minimum number in tuple9 is:", min(tuple9))
print("Maximum number in tuple9 is:", max(tuple9))
print("Sum of all numbers in tuple9 is:", sum(tuple9)) #uh cant use sum function for string tuple, it will give error

#------immutable nature of tuple----------------
#for example 1st i do lin list then same as tuple
list1=["Sheikh","Abdur","Rehman","Sahb"]
list1[3]="sir" #we can change the value of list because list is mutable
print(list1)
#Now i do same thing with tuple
tuple11=("Sheikh","Abdur","Rehman","Sahb")
#tuple11[3]="sir" #we cant change the value of tuple because tuple is immutable, it will give error
print(tuple11)

#-----sorting in tuple ,as we know tuple is immutable, so we cant sort the tuple but we can sort the list which is created from the tuple
tuple12=(5,2,9,1,4)
list12=list(tuple12) #convert tuple to list
list12.sort() #sort the list
print(list12)
tuple12=tuple(list12) #convert sorted list back to tuple
print(tuple12)