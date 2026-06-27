# num=int(input("Enter the number : "))
#--------Even & odd check --------
#if num%2==0:
#    print(num, " is even ")
#else:
#    print(num, " is odd ")

#---------Allow greater than or equal to 18 & less than 50 years of age
# if(num>=18 and num<=50):
#     print("You are allowed to enter")
# else:
#     print("You are not allowed to enter")

# if(num>=5000):
#     print("yeahhhh ! you won 500$ voucher")
# elif ( num>=2500):
#     print("yeahhhh ! you won 250$ voucher")
# else:
#     print("oopps! you are not eligible for voucher")

#----------iterate a list ----------
# list1=[1,2,3,4,5]
# for i in list1:
#     print(i)

#----------iterate a string ----------
# str1="I am Abdur Rehman"
# for i in str1:
#     print(i)

#------------iterate a dictionary ----------
# dict1={"name":"Abdur Rehman","age":25,"city":"Karachi"}
# for i in dict1.items():
#     print(i)
    
#-------iterate over a range of numbers --------
# for i in range(2,9):
#     print(i)

#------list comprehension --------
list1=[1,2,3,4,5]
list2=[]
for i in list1:
    list2.append(i**2) #Square of each element in list1 and append to list2
print(list2)