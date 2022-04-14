# this program display information about time 
# Version 1.1.0
import datetime , os , time
x = datetime.datetime.now()
hour = int(x.strftime("%H")) * 60
minute = int(x.strftime("%M"))
def timer(): 
    print('Year:', x.strftime('%Y'))
    print('Day: ', x.strftime('%j'))
    print( 'Minutes Passed:', hour + minute)
    print('Minutes Remains:', 1440 - ( hour + minute))

while True:
    timer()
    time.sleep(10)
    # os.system('clear') # "Clear doesn't work"
    # print(chr(27)+'[2j') # this also doesn't work
    # print('\033c') # this also doesn't work
    # print('\x1bc') #this also doens't work too