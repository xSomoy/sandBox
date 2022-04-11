import datetime
import time
x = datetime.datetime.now()
hour = int(x.strftime("%H")) * 60
minute = int(x.strftime("%M"))
def timer(): 
    print(x)
    print( 'Minutes Passed:', hour + minute)
    print('Minute Remains:', 1440 - ( hour + minute))

while True:
    timer()
    