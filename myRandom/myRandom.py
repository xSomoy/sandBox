# importing datetime module for now()
import datetime
 
# using now() to get current time
current_time = datetime.datetime.now()
y = int(input("Enter Random Number Lenght: "))
a = int(input('Input Random Seed: ')) + current_time.hour
b = int(current_time.minute) + a
c = int(current_time.month) + b
d = int(current_time.year) + c

x = int((((a+b+c+d) - (a-b-c-d) * (a*b*c*d) / (a/b/c/d)) + 1 ) / 16)

while len(str(x)) > y:
    x = x / len(str(x))
    print(x)
print(x)