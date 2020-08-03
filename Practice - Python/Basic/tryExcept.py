

try:
    value = 10 / 0
    number = int(input("Enter A Number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")