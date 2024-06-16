#PALLINDROME-NUMBER
# Input: 12321

num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
# Output: Palindrome



#PALLINDROME-STRING

st=input('Enter string value:')
rev=st[::-1]
if rev==st:
    print('string is pallinndrome')
else:
    print('non-pallindrome')

# REVERSING A STRING WITHOUT USING SLICING.

a = 'madam'
result = ''
i = 0
while i < len(a):
    result = a[i] + result
    i=i+1
if a==result:
    print("pallindrome")
else:
    print("non-pallindrome")
