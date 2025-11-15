marks1= 34
marks2=32
marks54=78
marks = [34,35,35,3,5,67]
print(marks[1])
print(type(marks))
print(len(marks))
num1 = ["asmit",2,3,4,"boy"]

# num2 = 3
# num2[0]= "asmit" cant be run because string and int are immutable
# but list are mutable

print(num1[4])

# sublist{List slicing}
# list name[starting indx:ending index] ending index include nahi hota

print(marks[1:6])
print(marks[-1:-6])
#----------------------------------------------------------------------------
# LIST METHOD:
# list.append(4)-- adds a element - {4}  in list at the end
# list.sort() ---- sorts in ascending order 
#list.reverse() ---- it reverses the whole list
#list.insert(idx,el)--- insert a element at index 
# you cannot print the list function directly by calling it inside print ()
#list.remove(2) ---- removes only first occurence of element 
#list.pop(idx) --- removes element at idx
#-----------------------------------------------------------------------------

listz = [4,73,34,54,5,56,79,18]

listz.append(4)
print (listz)

listz.sort()
print (listz)

listz.sort(reverse = True)
print (listz)

listz.insert(2,45)
print(listz)

listz.remove(4)
print (listz)

listz.pop(3)
print(listz)
tup = (23,43,554,3,22,1,3,5)
#____________________________________________________________________________
#u can usedogle as string and int and float but once u use comma(,)than it is defaultdogle
#tup slicing is same as list we use same box and same format
#tup method 
#well indog you have to declare the function in print function to print
print(tup.index(3))
print(tup.count(3))

