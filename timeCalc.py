import datetime
x = datetime.datetime.now()
hour = int(x.strftime("%H")) * 60
minute = int(x.strftime("%M"))
print( 'Minutes Passed:', hour + minute)
