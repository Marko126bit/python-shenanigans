
name = input("Dobrodosli, vase ime molim?\n")

if name == "Milos" or name == "Zeljana":
 evil_status =input ("el ces da budes dobar?\n")
 good_deeds = int(input ("zadnja sansa, koliko si dobrih stvari uradio/la\n"))
 if evil_status == "ne" and good_deeds < 4 :
  print("vrata su ti levo, cao.\n")
  exit() 
   #exit zavrsetak ako je if tacan ili obrnuto
  
 else :
   print("hello " + name +  " ,Thank you so much for coming here.\n\n\n")
   #exit zavrsetak ako je if tacan ili obrnuto
   
else:
 print("hello " + name +  " ,Thank you so much for coming here.\n\n\n")