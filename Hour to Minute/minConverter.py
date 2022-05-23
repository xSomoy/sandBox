# By Mushphyqur Rahman Tanveer
# Who wrote this script on a toilet while pooing
# And finished before his dump went down
# @140923052022
# Version 1.0.0


foo = input("Enter Time [hhmm]:")
if  len(foo) < 4:
	print("Format Error")
else:
	foo = (int(foo[0]+foo[1]) * 60 ) + int((foo[2] + foo[3]))
	print("Time in Minutes:",foo)
