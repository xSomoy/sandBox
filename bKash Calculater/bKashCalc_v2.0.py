# bKash Calc V2.0
# Author  : Mushohyqur Rahman Tanveer

# Taking input
a = int(input('Amount: '))

# Charge in %
pAgent = 1.49
agent = 1.85
atm = 1.49
bank = 1.25

copa = (a * pAgent) / 100
print('Prio Agent: ' + str(copa))

coa = (a * agent) / 100
print('Agent: ' + str(coa))

coatm = (a * atm) / 100
print('ATM: ' + str(coatm))

cobank = (a * bank) / 100
print('Bank: ' + str(cobank))
