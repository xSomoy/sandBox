employeeFile = open("employees.txt", "r")
# print(employeeFile.readable())
# print(employeeFile.readline())
for emp in employeeFile.readlines():
    print(emp)
employeeFile.close()