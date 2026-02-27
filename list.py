my_list1=[]
my_list2=list()
number=[1,2,3,4,5]
fruits=["banana","apple","cherry"]
mixed=[1,2,3,"python",3.14,True]
print(my_list1)
print(my_list2)
print(number)
print(fruits)
print(mixed)

# list with nested list
nested_list =[[1,2,3],["banana"],["true","false"],] 
print(nested_list)

#list using list constructors
list_from_tuple =list((1,2,3))
string_to_list=list("python")
print(list_from_tuple)
print(string_to_list)

#Accessing elements in a list
#using indexing
my_list3=["python","java","c"]
print(my_list3[0])
print(my_list3[1])

#using sciling
number1=[1,2,3,4,5]
print(number1[1:4])
print(number1[:3])
print(number1[2:])
print(number1[-3:-1])
print(number1[::-1])

#Modifing list
#changing elements
number[2]=100
print(number)

#Adding elements
number.append(50)
number1.insert(2,88)
print(number)
print(number1)

#Removing Elements
num = [10,20,30,40,50]
num.remove(10)
num.pop(2)
num.pop()
del num[1]
print(num)
