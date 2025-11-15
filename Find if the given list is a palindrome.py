List1=[]
a =input("write 1 thing for list:")
b =input("write 2 thing for list:")
c =input("write 3 thing for list:")
List1.append(a)
List1.append(b)
List1.append(c)
List2 = List1.copy()
List1.reverse()
if List1 == List2 :
    print("Its a palindrome")
else :
    print("its not a palindrome")
#-------------------------------------
# another way i think
List1=[]
List2 =[]
List2 == List1
a =input("write 1 thing for list:")
b =input("write 2 thing for list:")
c =input("write 3 thing for list:")
List1.append(a)
List1.append(b)
List1.append(c)
List1.reverse()
if List1==List2:
    print("Its a palindrome")