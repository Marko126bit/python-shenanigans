#inzinjerske plate bez engleskog
p = print

name_1 = "Milos"
name_2 = "Dejan"
name_3 = "Marko"

plata_1= 260000
plata_2= 590000
plata_3= 480000

p(name_1 + " ima platu od " + str(plata_1) + "\nnjegov kolega " +  name_2  +" ima platu od " + str(plata_2))
p("Tu je i " + name_3 + " sa platom od " + str(plata_3))

Porez_na_pamet = 50000 * 3

neto = plata_1 + plata_2 + plata_3 - Porez_na_pamet

p ("svi imaju jedan kljucni problem a to je porez koji skida 50000.Uracunavajuci sve 3 plate sa porezom iznosi: $" + str(neto) + " neto sa sve 3 plate zajedno.U svakom slucaju. \n")
p (name_1 + " nema pare za ps5 " + name_2 + " nema pare za teslu, a " + name_3 + " nema pare za trotinet koji je na snizenju :(.")

