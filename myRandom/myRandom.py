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

# check for 0 lenght input error correction
# wrap the whole thing as a function
# if the function is not provided required argument then execute user input option
# make the whole thing as a module or something so that it can be used in other programs