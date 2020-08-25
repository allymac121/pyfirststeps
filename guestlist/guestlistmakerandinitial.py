#create a file that you can write all your guestnames into

myfile = open("wendallbirthday.txt","w")

#write into the guestlist
myfile.write("Mellissa fumero,vegan\n")
myfile.write("Donatello bonucci,cool\n") 
myfile.write("Albertini francis,cool\n")
myfile.write("Eulysis collin,vegan\n")
myfile.write("Doyle Monsanto,vegan\n")
myfile.write("Joan Injira,cool\n")
myfile.write("Sergi reberto,cool\n")
myfile.write("Martin tyler,cool\n")

#close the file always as good practise
myfile.close()