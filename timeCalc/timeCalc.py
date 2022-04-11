# this program display information about time 
# Version 1.0.1
import datetime , os , time
x = datetime.datetime.now()
hour = int(x.strftime("%H")) * 60
minute = int(x.strftime("%M"))
def timer(): 
    print('Year:', x.strftime('%Y'))
    print('Day: ', x.strftime('%j'))
    print( 'Minutes Passed:', hour + minute)
    print('Minute Remains:', 1440 - ( hour + minute))

while True:
    timer()
    time.sleep(10)
    os.system('cls')
    