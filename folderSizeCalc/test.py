import datetime

now = datetime.datetime.now()

print("Current date and time:")
print(now)

print('\n\n\n')
# Display only the date
print("Current date:", now.date())

# Display only the time
print("Current time:", now.time())

# Display the date and time in a custom format


print('\n\nDate and Time formating\n')

print(str(now.date()).replace("-",""))
print(str(now.time())[:-9].replace(":",""))
print('\n\n\n\n')


# date time solution 
print('\n\nformating\n')
print(now.strftime("%H%M%d%m%y"))