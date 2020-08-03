def raiseToHell(baseNum, powNum):
    result = 1
    for index in range(powNum):
        result = result * baseNum
    return result

print(raiseToHell(3, 2f))
