#There are 6 data types in python : numbers(int/float/complex/bool),string,list,dictionary,tuple and set

#NUMBERS : 
 
x=15      #integer
y=15.34   #float
z=15j     #complex 
print(type(x))   #type function if used to check data types of variables


#STRING: immutable , we use either ('') or (" ")

#create a string 
str='Today is Tuesday'
print(str)
print("Directly print the string")

#Printing lenght of string: len(string_name)
print(len(str))

#Access string elements : string index starts from 0 , string_name[index]
print(str[0]) #first element
print(str[-1]) #last element 

#String Slicing : string_name[starting_index:ending_index]
print(str[2:4]) #printing characters between 2nd and 4th index
print(str[:3]) 
print(str[2:])

#Uppercase and Lowercase : string_name.upper() , string_name.lower()
print(str.upper())
print(str.lower())


#LIST : mutable , heterogeneous , dynamic , list_name=['',''] , allows duplicates 

#creating a list
eg=['apple',10,'banana']
print(eg)

#append : list_name.append(element) i.e.lists are dynamic in nature
eg.append(5)
print(eg)

#inserting at a particular index : list_name.insert(index,element)
eg.insert(3,'mango')
print(eg)

#reverse the list : list_name.reverse()
eg.reverse()
print(eg)


#DICTIONARY : key:value pairs , ordered , mutable , doesnt allow duplicates , dict_name={ key : value , key :value}

#creating a dictionary
dict={'a':'apple',2:'banana','third':'mango'}
print(dict) 

#Accessing elements in dict : use keys as indexes or get() 
print(dict['third']) 
print(dict.get('a'))

#updating dictionary 
dict[2]='pineapple'
print(dict)

#adding element
dict['forth']=15
print(dict)

#TUPLE : immutable , ordered , heterogeneous , allows duplicate entries , tuple_name=('',"")
#creating a tuple 
tup=(10,'red','green',17,34,50,'yellow','red')
print(tup)

#accessing elements inside a tuple
print(tup[1])
print(tup[-1]) #in above example , we print duplicate values to verify whether tuple allows duplicate entries 

#count() can be used to count duplicate entries , tup_name.count(element_name)

#SET : unindexed , unordered , immutable , duplicates not allowed 
#creating a set
s={'tree',3,57,'apple',57,True,1} #True and 1 / False and 0 are considered as same so duplicates are not printed 
print(s)








