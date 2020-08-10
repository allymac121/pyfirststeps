#declare the key variables
country = ""
ordertotal = 0
ordertotal = 0

#list the countries and their respective import duty(this is off the top of my head)
ke = .30
usa = .20
Le = .40
Wa = .01
Esp = .45


#ask for their country in ordertotal to get the tax rate applicable
country = input("where do you come from ? ")

#get the total ordertotal
ordertotal = float(input("what was your shopping total?"))

#calculate what they will actually pay including the tax

if country == "kenya":
    ordertotal = ordertotal + ordertotal * ke
elif country == "america":
    ordertotal = ordertotal + ordertotal * usa
elif country == "lebanon":
    ordertotal = ordertotal + ordertotal * Le
elif country == "wakanda":
    ordertotal = ordertotal + ordertotal * Wa
elif country == "spain":
    ordertotal = ordertotal + ordertotal * Esp
else:
    print("we can't compute that at the moment")


#print their grand total as follows
print("your total is going to be : %2f"%ordertotal)

input("press enter to exit")
