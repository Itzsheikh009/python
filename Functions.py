#----even-odd check
num=int(input("Enter the number : "))
# def even_odd(num):
#     if(num%2==0):
#         print(num," is even")
#     else:
#         print(num," is odd")
        
# even_odd(num) #Calling the function with argument num    

#----Factorial of a number
# def fact(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#         fact=1
#         for i in range(1,num+1):
#             fact=fact*i
#         return fact

# print(fact(num))

#----sum of all natural numbers 
# def natural_sum(num):
#     sum=0
#     for i in range(1,num+1):
#         sum=sum+i
#     return sum

# print(natural_sum(num))

#_---_--_-__--Lambda function   ((  lambda arguments : expression  )) _-_-_--_---____----___----_-___

#create  a function that add 10 to a number

# result=lambda num : num+10
# print(result(num))

#create a lambda function thats check that the number is even or odd

# result=lambda num : (num,"is even") if num%2==0 else (num," is odd")
# print(result(num))

#create a lambda function that add two integers 
num2=int(input("Enter the second number : "))
result= lambda num,num2 : num+num2 
print("Sum of Num 1 & num2 is : ",result(num,num2))