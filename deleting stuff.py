#method



lefkada_accesories = [" test "," e - scooter ", " vegeta" , " quad bike" , " good tomatoes " , 
" laptop" , " powerbank" , " sun protector "
, " luggage" , " ball " , " mythos beer " ]

#print(lefkada_accesories)

#putting methods in to a list
lefkada_location = ["Egremni" , 10 , 27.5 , True]

lefkada_accesories.append("toilet paper")

lefkada_accesories.extend(["bidet" , "plunger"])

lefkada_accesories = lefkada_accesories + ["cif" , "soap"]

lefkada_accesories.insert (0, "razor")

lefkada_accesories.insert (-16 ,"shawing cream")

#deleting stuff

#lefkada_accesories.clear()

#lefkada_accesories.remove("plunger")

#lefkada_accesories.remove ("vegeta")

print("i deleted this : " + lefkada_accesories.pop ( 0 ))

lefkada_accesories.pop ( 0 )

print(lefkada_accesories)