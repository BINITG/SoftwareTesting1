#STRING OPERATIONS


st="My Name Is Binit Kumar"
print(st.upper())
print(st.lower())
print(st.replace("My","Binit"))
print(st.count("a"))
print(st.find("B"))
print(st.split("N"))




#LIST OPERATIONS


list=["apple","banana",2,4,6]
list.append("binit")                #ADD NEW ELEMENT IN LAST
print(list)
#list.pop(2)                        #DELETE ELEMENT
print(list)
#list.reverse()                     #REVERSE A LIST
print(list)
list.insert(3,"mango")               #INSERT AT A PARTICULAR INDEX POINT
print(list)
list.sort()                          #SORT ALPHABETICALLY
print(list)



#DICTIONARY OPERATIONS

fruit={"apple":2,"banana":4,"guava":6,"mango":8}
print(fruit.keys())
print(fruit.values())
print(fruit["mango"])
print(fruit["apple"])
fruit.pop("apple")
print(fruit)



#SET OPERATIONS

set={1,"a",True,2,"b",False}
set.add("hello")
print(set)
set.update([12,13,14])
print(set)
set.remove("b")
print(set)

S1={1,2,3}
S2={"A","B","C",1}
S3=S1.union(S2)
print(S3)
S4=S1.intersection(S2)
print(S4)

#STRING OPERATIONS