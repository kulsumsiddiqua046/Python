DATE : 23/08/2025
#create an empty list
emptyList=[ ]
print(emptyList)

#list of int type
integerList=[20,30,50,70]
print(integerList)

#list of string tyoe
stringList=['John','London','COP']
print(stringList)

#list of mixed type
mixedList=['Harry','Hogwarts',1005,30,'Gryfindor']
print(mixedList)

#list of nested type
nestedList=[1,2,3,4,['Hello' 'Harry'],6,7]
print(nestedList)

#access an element from the list
std_list=['Zoha','CSE(AI)',4035,72350126169,'Hyderabad']
std_list[3]
 

 #add an element to a list
my_list=['Hello']
my_list.append('world')
print(my_list)

#remove an element from the list
num_list=[20,30,40,50,60]
num_list.pop(3)
print(num_list)

#insert an element into the list
mList=[100,2000,30000]
mList.insert(2,90)
print(mList)

#get index of the first item
std_list=[20,30,40,50,60]
std_list.index(40)
print(std_list)

#find length of the list
fam_list=[29,50,10,40,79]
print(len(fam_list))
print(fam_list)

#count occurence of any item in the list
bestList=[51,47,64,35,51,301,51,29,51]
print(bestList.count(51))

#reverse the list
nameList=[12,31,58,34,99,11]
print(nameList[::-1])

#remove and return item at index
numbers=[1,2,3,4,5,6,7,8,9,10]
numbers.remove(10)
print(numbers)

#print the list elementwise
clg_list=[4001,4002,4003,4005]
for item in clg_list:
    print(item)
