num1 = float(input("Enter First Number:"))
op = input("Enter Operator Number:")
num2 = float(input("Enter Second Number:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")