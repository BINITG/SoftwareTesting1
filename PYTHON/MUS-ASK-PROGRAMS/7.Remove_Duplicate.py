# REMOVE DUPLICATE VALUE FROM LIST

list1 = [1, 2, 3, 4, 2, 5, 6, 1]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# REMOVE DUPLICATE FROM STRING
str1= "APPLE"
str2=''
for i in str1:
    if i not in str2:
        str2+=i
print(str2)

