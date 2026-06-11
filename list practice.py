list=["Abdur Rehman",2009,22,"Python"]
print(type(list))
#---------------------------------------
tuple2=("Abdur Rehman",2009,22,"Python")
print(type(tuple2))
print(len(tuple2))
print(tuple2[2])
#---------------------------------------nested list
nested_list=[1,2,3,[4,5,6],7]
print(nested_list)
print(len(nested_list))
print(nested_list[3])
#i only need 6 now what i do?
print(nested_list[3][2])
print(nested_list[-3])

#------------------------------ Concatination of list
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

#---------------------------Membership in list
print(3 in list1)
print(10 in list1)

#---------------------------list mutability
list5=["lahore","karachi","islamabad"]
list5[1]="faisalabad"
print(list5)

#---------------------------list extend & append
list6=[1,2,3]
list6.extend([4,5,6])
print(list6,"and length becomes ",len(list6))

list7=[1,2,3]
list7.append([4,5,6,"shutup"])
print(list7,"and length becomes ",len(list7))

#---------------------------Del command
list8=[1,2,3,4,5]
del list8[3]
print(list8)

#----------pop & remove pop works on index and remove works on value
list9=[1,2,3,4,5]
list9.pop(2)
print(list9)

list10=[1,2,3,4,5]
list10.remove(3)
print(list10)

#-------------Sort ( it will sort in ascending order by default) called dot sort

list11=[44,23,54,76,11,9]
list11.sort()
print(list11)

list12=[44,23,54,76,11,9]
list12.sort(reverse=True) 
print(list12)

