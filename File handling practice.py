#_-----____--__-- open a file

# file=open('D:\\Udemy\\Python\\Sample.txt','r')

# for line in file:
#     print(line)


#-----__----____-___-____--_-reading a file
# print(file.read(16))

#Readline function
# print(file.readline(3))

file=open('D:\\Udemy\\Python\\Sample.txt','w')
file.write("i am abdur rehman,, \n")
file.write("Whats your name ; ??")
file.close()
file=open('D:\\Udemy\\Python\\Sample.txt','r')
print(file.read())
