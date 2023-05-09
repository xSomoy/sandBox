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
print("Formatted date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

print('\n\nDate and Time formating\n')

print(now.date())
print(str(now.time())[:-9].replace(":",""))