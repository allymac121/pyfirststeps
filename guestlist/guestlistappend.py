#create a file that you can append new guestnames into

myfile = open("wendallbirthday.txt","a")

#Write the guest names and ages to the file
for index in range(4) :
    name = input("Enter guest name: " )
    foodchoice = input("Enter guest food choice: " )
    myfile.write(name + "," + foodchoice  + "\n")

#Close the file
myfile.close()