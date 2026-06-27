import numpy as np
# a=np.array([1,2,3,4,5])
# print('Array is : ', a)
# print(type(a)) #ndarray  means n dimentional array

#---------------------------------------------------------

# a=np.array([[1,3,5,7,9],[2,4,6,8,10]])
# print("2D Array is : ",a)
# print(type(a))
# print(len(a))
# #For checking dimentions 
# print("The array has ",a.ndim," Dimentions.")

#----------------------------------------------------------

# a=np.array([[[[2,3,4,5,6],[4,6,7,8,9],[7,8,9,11,13]]]]) #Elements must be same 
# print(a)
# print("The Array Has ",a.ndim," Dimentions.")
# print(a.shape)
# # Shape = (1, 1, 3, 5)
# # 1st 1 --> size of the outermost dimension
# # 2nd 1 --> size of the second dimension
# # 3rd 3 --> number of rows
# # 4th 5 --> number of columns

#------------------------------------------------------------

# #FOR Specific Element

# print(a[0,0,1,4])#row
# print(a[0,0,:,2])#column

#------------------------------------------------------------

# #Changing element
# a[0,0,2,4]=99
# print(a)

#--------------------------------------------------------------

#Zeros & ONe's Method in numpy
# b=np.zeros((3,3))
# print(b)

# c=np.ones((4,4),dtype='int')
# print(c)
# print(type(c[1,2]))

#---------------------------------------------
# #Full method
# a=np.full((3,3),99,dtype=('double'))
# print(a)

#Random matrix

# print(np.random.rand(4,4))
# print(np.random.randint(3,6,size=(3,5)))
print(np.identity(4))