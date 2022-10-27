a = input("How much you want to cash out?: ")
def cashOutCalc(b):
    b = int(b)
    commisionRate = 1.85
    totalCommision = (b * commisionRate) / 100
    returnCash = b - totalCommision
    print('Return Cash: ' +  str(returnCash))
cashOutCalc(a)

