#TO PRINT GIVEN NUMBER OF *s IN A ROW.

n=int(input('enter n value:'))
for i in range(n):
    print('* ',end=' ')
#TO PRINT *s FORM SQUARE.

n=int(input('enter no. of rows:'))
for i in range(n):
    print('* '*n)

#1 1 1
#2 2 2
#3 3 3

n=int(input('enter no. of rows:'))
for i in range(n):
    print((str(i+1)+' ')*n)
#A A A A
#B B B B
#C C C C
#D D D D

n=int(input('enter no. of rows:'))
for i in range(n):
    print((chr(65+i)+' ')*n)


#TO PRINT RIGHT-ANGLED TRIANGLE.

n=int(input('enter no. of rows:'))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

#TO PRINT INVERTED RIGHT-ANGLED TRIANGLE.

n=int(input('enter no. of rows:'))
for i in range(n):
    print('* '*(n-i))

#TO PRINT PYRAMID PATTERN WITH * SYMBOLS.

n=int(input('enter no. of rows:'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))

#TO PRINT INVERTED PYRAMID.

n=int(input('enter no. of rows:'))
for i in range(n):
    print(' '*(i)+'* '*(n-i))

#TO PRINT DIAMOND PATTERN WITH * SYMBOLS.

n=int(input('enter n value:'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-i-1))


