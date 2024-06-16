num = int(input("Enter a number: "))
# Input: 407
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp = temp // 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
# Output: 407 is an Armstrong number

#What is an armstrong number?

#125=(1**3)+(2**3)+(5**3)=1+8+125=134 =no armstrong
#153=1+125+27=153=armstrong no.
