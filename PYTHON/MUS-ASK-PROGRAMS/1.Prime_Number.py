#prime no.=2,3,5,7
#def=number which divided by  only 1 and (itself)

num = int(input("enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
# 23 is a prime number