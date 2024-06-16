num=5
factorial=1
if num<0:
    print("factorial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial=factorial*i
print("the factorial of",num ,factorial)


'''RECURION

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
num=5
print("factorial of ",num,"is",factorial(num))'''
