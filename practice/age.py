#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Enter Name : ")
age = int(input("Enter age : "))
copies = int(input("Number of copies : "))
a =0
while(a<copies):
    print(name +" will be 100 years old at "+str(2023-age+100))
    a+=1
