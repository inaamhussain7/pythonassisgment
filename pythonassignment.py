mixedlist=[10, 25, 3, 18, 50,3.14, 2.718, 1.618, 0.577, 9.8,"apple", "banana", "cherry", "date", "elderberry"]
print(mixedlist)
#this will print the original list cointaing float,interger and string
mixedlist.append(67)
print(mixedlist)
#this will print the original list along with 67 added to the last index
print("new list")
#this will indicate a new list is created for the 3rd question
newlist=[]
print(newlist)
newlist.insert(0,20)
#the 0 stands for index and 20 is the element
newlist.insert(1,19)
#the 1 stands for the index and 19 is element
newlist.insert(2,18)
newlist.insert(3,17)
newlist.insert(4,16)
newlist.insert(5,15)
newlist.insert(6,14)
print(newlist)
#this will print the newlist after the new elements are added
print("the elements of mixedlist")
for i in mixedlist:
 print(i)
#this will show all the elements of mixedlist
print("integerlist")
integerlist=[94,68,77,17,23,44,89,69,24,43]
print(integerlist)
#this will be used to compare the sorted list
print("sorted in ascending order")
integerlist.sort(reverse=False) #sorts in ascending order
print(integerlist)
print("sorted in descending order")
integerlist.sort(reverse=True) #sorts in descending order
print(integerlist)
print("stringlist")
stringlist=["abc","abdul","rashid","majid","ali","ahmad"]
#this will be used to compare to sorted list
print(stringlist)
print("sorted in ascending order")
stringlist.sort(reverse=False) #sorts in ascending order
print(stringlist)
print("sorted in descending order")
stringlist.sort(reverse=True) #sorts in descending order
print(stringlist)
emptylist=[]
pos=int(input("inter any position"))
val=int(input("inter any value"))
emptylist.insert(pos,val)
for i in emptylist:
 print(i)
print("the maximum value of integer list")
print(max(integerlist)) #shows the maximum valued element in list
print("the minimum value of integer list")
print(min(integerlist)) #shows the minimum valued element in list
#we will take x as a variable for the addition of two lists
x=integerlist + newlist
print(x)
#this x will show a combined list of integer list and new list















