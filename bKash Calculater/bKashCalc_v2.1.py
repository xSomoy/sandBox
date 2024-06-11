# bKash Calc V2.1
# Author  : Mushohyqur Rahman Tanveer

#Taking input
a = int(input('Amount: '))

# Charge in %
pAgent = 1.49
agent = 1.85
atm = 1.49
bank = 1.25

copa = (a * pAgent) / 100
print('Prio Agent: ' + str(copa))
print('=> Hard Cash:' + str(a - copa))

coa = (a * agent) / 100
print('Agent: ' + str(coa))
print('=> Hard Cash:' + str(a - coa))

coatm = (a * atm) / 100
print('ATM: ' + str(coatm))
print('=> Hard Cash:' + str(a - coatm))

cobank = (a * bank) / 100
print('Bank: ' + str(cobank))
print('=> Hard Cash:' + str(a - cobank))
