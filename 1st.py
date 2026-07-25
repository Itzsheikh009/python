name=input("What's your name : ")
age=int(input("Enter the age : "))
if age >=20:
    print(name," You can play.")
else:
    print(name," You can not play.")
    exit()
password=input("Enter the password : ")
if(password == "09"):
    print("The password is correct :)")
else:
    print("The password is incorrect :(")
    print("Please enter the Correct password .. ")
    exit()

print(" ------- .. Welcome To KBC.. -------")
questions =[
["How many provinces in pakistan ?",2,3,4,5,4],
["How many cities in pakistan ?",190,230,200,50,3],
[ "Largest papulation province of pakistan","punjab","Sindh",
  "Balochistan","Kpk","giggit baltistan","Azad Kashmir",1],
["Capital of Pakistan?", "Karachi", "Islamabad", "Lahore", "Peshawar", 2],
["National language of Pakistan?", "Urdu", "Punjabi", "Sindhi", "English", 1]  ,
["Currency of Pakistan?", "Rupee", "Dollar", "T akka", "Dinar", 1],
["Founder of Pakistan?", "Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Ayub Khan", 3],
["National sport of Pakistan?", "Hockey", "Cricket", "Football", "Kabaddi", 1],
["Highest mountain in Pakistan?", "Nanga Parbat", "K2", "Mount Everest", "Broad Peak", 2],
["Which sea touches Pakistan?", "Arabian Sea", "Black Sea", "Red Sea", "Caspian Sea", 1],
["National flower of Pakistan?", "Rose", "Sunflower", "Jasmine", "Tulip", 3],
["First Prime Minister of Pakistan?", "Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Ayub Khan", "Benazir Bhutto", 1],
["When did Pakistan get independence?", 1930, 1945, 1947, 1950, 3],
    ["most papular leader of pakistan in 21st century","Nawaz Sharif","Benazir Bhutho","Imran khan"," Mariam nawaz",3]
            ]

levels=[1000,3000,5000,10000,20000,40000,80000,
    160000,320000,640000,1250000,2500000,500000,10000000]
money=0
i=0
for i in range (0,len(questions)):
    question=questions[i]
    print("\nQuestions for Rs. ",levels[i])
    print(question[0])
    print("A.",question[1],"        " "B.",question[2],)
    print("C.",question[3],"        " "D.",question[4],)
    reply=int(input("Enter Your Answer (1-4) or 0 For Quit :"))
    if(reply==0):
        money=levels[-1]
        break
    if(reply==question[-1]):
        print("Correct Answer,uh have won Rs",levels[i])
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==13):
            money=10000000

    else:
        print("Wrong Answer ! ..")
        break
print("congrats ",name," You won total Rs.",money,"/-")