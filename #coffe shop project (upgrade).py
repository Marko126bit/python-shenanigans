#coffe shop project
p = print
#lets make our coffe barista
print("hello welcome to our coffe shop") 

#ime = unos + pitanje
name = input("what is youre name sir?\n")

#bitno!!!! (if konfiguracija) 
#or = ili
if name == "Milos" or name == "Zeljana":
 evil_status =input ("el ces da budes dobar?\n")
 if evil_status == "da":
  print("ok ajde upadaj\n")
 
  if evil_status == "ne":
   p("smaras me "+ name + " izlazi napolje") 
 #exit zavrsetak ako je if tacan ili obrnuto
   exit()
else:
 print("hello " + name +  " ,Thank you so much for coming here.\n\n\n")
#name = "customer"
#print (name)
#name = "crackhead"
#print("crackhead")
#meni = proizvodi 

menu = "coffe,latte,cookie,srpska kafa"

# print slike unosa (ime + pitanje odvlaka + meni)
print(name +",what would you like to order?,here is our menu\n" + menu)

#if u if,if nesting
order = input()
#elif = if + else
if order =="srpska kafa":
 price = 3
elif order =="cookie":
  price = 4
elif  order == "latte":
  whipped_cream = input("would you like some whipped cream?\n")
  if whipped_cream == "yes":
   price = 16
  else: 
    whipped_cream == "no"
    price = 8

quantity= input("how many coffees would you like sir\n")
#int= + , - ,* , /.
total= price * int(quantity)

print("thank you. Your total is : $" + str(total))

print("\n sounds very good " + name + " well have your "+ quantity +" "+ order + " ready for you in a moment")



