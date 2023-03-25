#Lefkada vacation 2023

#LIST []             TEST = 0
lefkada_accesories = [" test "," e - scooter ", " vegeta" , " quad bike" , " good tomatoes " , " laptop" , " powerbank" , " sun protector "
, " luggage" , " ball " , " mythos beer " ]

#print(lefkada_accesories)

lefkada_location = ["Egremni" , 10 , 27.5 , True]

me = lefkada_accesories [1] +  lefkada_accesories[3]
#print(me)

Dejan = lefkada_accesories [10] + lefkada_accesories[5] 
#print(Dejan)

Milos = lefkada_accesories [5] + lefkada_accesories [6]
#print(Milos)

group = ("we are going on a vacation " + Milos +(" was brought by Milos and the ") + Dejan + (" was brought by Dejan, lastly " + me + (" was brought by Marko \n")))

print(group)

planning_in_style = (" There are " + str(lefkada_location [1]) + " people on the vacation, the weather is going to be " + str(lefkada_location [2]) + " and the first location is going to be " + lefkada_location[0])

print (planning_in_style)