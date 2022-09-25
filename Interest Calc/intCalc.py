# Rules 30k interest on 100k loan for 12months
# find out the interest rate now

from multiprocessing import current_process


rate = 0.025
loanAmount = float(input("how much did you loan?: "))
months = float(input("how many months have passed?: "))
currentInterest = rate * loanAmount * months
totalDue = loanAmount + currentInterest
print("Your Current Interest is: " + str(currentInterest) + " BDT" )
