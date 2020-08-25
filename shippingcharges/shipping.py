Ordertotal = 0
shippingcost = 0
orderwithshipping = 0

Ordertotal = float(input("what is the order total for purchases made?"))

if Ordertotal <= 100:
    shippingcost == 0

else:
    shippingcost = 20

orderwithshipping = Ordertotal + shippingcost

print("your final total,including sjipping is: {}".format(orderwithshipping )


