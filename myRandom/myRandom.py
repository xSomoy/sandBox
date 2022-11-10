# importing datetime module for now()
import datetime
 
# using now() to get current time
current_time = datetime.datetime.now()
y = int(input("Enter Random Number Lenght: "))
a = int(input('Input Random Seed: ')) + current_time.microsecond
b = int(current_time.second) + a
c = int(current_time.minute) + b
d = int(current_time.hour) + c

x = int((((a+b+c+d) - (a-b-c-d) * (a*b*c*d) / (a/b/c/d)) + 1 ) / 16)

while len(str(x)) > y:
    x = int(x / len(str(x)))
print(x)