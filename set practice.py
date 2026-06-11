#Set does not allow duplicate values
myset = {1,4, 2,1,5, 3,4,5, 4, 5, 5}
print(len(myset)) #it will print 5 because it does not allow duplicate values
print(myset)

#convert list into set
mylist = [1,2,3,4,5,1,2,3,6,4,2]
myset2 = set(mylist)
print(myset2) #it will print {1, 2, 3, 4, 5, 6} because it does not allow duplicate values

#------add &remove element in set----------------
set4={1,2,3,4,5}
set4.add("Karachi")
print(set4)
set4.remove(4)
print(set4)

#------------set operations ----------------
#union of sets
set1={0,1,2,3,4}
set2={3,4,5,6,7}
set3=set1.union(set2)
print(set3) #it will print {0, 1, 2, 3, 4, 5, 6, 7} because it combines all unique elements from both sets
#we can also write like this  
set3=set1 | set2
print(set3)

#--------Intersection of sets ----------------
set3=set1.intersection(set2)
print(set3) #it will print {3, 4} because it only includes elements that are in both sets
#we can also write like this
set3=set1 & set2
print(set3)

#--------Difference of sets ----------------
set3=set1.difference(set2)
print(set3) #it will print {0, 1, 2} because it
set3=set1-set2
print(set3)

#--------Symmetric difference of sets ----------------
set3=set1.symmetric_difference(set2)
print(set3) #it will print {0, 1, 2, 5, 6, 7} because it includes elements that are in either set1 or set2 but not in both
set3=set1 ^ set2
print(set3)