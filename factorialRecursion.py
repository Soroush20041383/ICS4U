#tail recursion or linear recurssion
def factorial(pNum):
    if pNum == 0:
        return 1
    else:
        return pNum * factorial(pNum - 1)
print(factorial(10))
