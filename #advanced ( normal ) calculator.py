#advanced ( normal ) calculator

num1 = float(input("enter the number\n"))
op = input("put youre operator\n")
num2 = float(input("enter the third number\n"))

if op == "+":
 print(num1 + num2)
elif op == "-":
 print(num1 - num2)
elif op == "*":
 print(num1 * num2)
elif op== "/":
 print(num1 / num2)
else:
 print("invalid operator.")
