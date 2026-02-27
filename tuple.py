empty_tuple = ()
single_tuple = (5)
multiple_tuple = ("python","true","1,2,3")
implicit_tuple = 1,2,3
print(empty_tuple)
print(single_tuple)
print(multiple_tuple)
print(implicit_tuple)

#Acessing Tuple Elements
#indexing
my_tuple =(10,20,30,40)
print(my_tuple)

#Negitive indexing
print(my_tuple[-1])

#slicing 
print(my_tuple[1:3])
print(my_tuple[:-1])
print(my_tuple[1:4])

#Operation on tuple
#Cancatenation
type1="sai"
type2="keerthi"
print(type1+type2)

#Repetation
print(type2*4)

#Membership Testing
my_tuple1=(1,2,3)
print(2 in my_tuple1)
print(5 not in  my_tuple1)

#Tuple Unpacking
my_tuple1=(1,2,3)
a,b,c=my_tuple1
print(a,b,c)

