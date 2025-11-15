num1=int(input("num1:"))
num2=int(input("num2:" ))
operator=(input("use operator:"))
def calculator(operator,num1,num2):
    if operator == '+':
     return  num1 + num2 
    elif operator == '-':
     return  num1 - num2
    elif operator == '*':
     return  num1 * num2
    elif operator == '/':
     return  num1 / num2
    else : print ("invalid input")
answer = calculator(operator,num1,num2)#here you cannot print direct calculator you have to call the function thrpoughj a variable than only you can print the variable 
print("Result",answer)