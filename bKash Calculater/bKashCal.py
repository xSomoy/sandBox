a = int(input("How much you want to cash out?: "))

def agentCat():
    agent= input("Priyo Agent? : ")
    if agent == 'yes':
        return 1.49
    else:
        return 1.85

def cashOutCalc(b):
    commisionRate = agentCat()
    totalCommision = (b * commisionRate) / 100
    returnCash = b - totalCommision
    print('Return Cash: ' +  str(returnCash))
cashOutCalc(a)

