
##    print("options:")
##    print("enter '+' to add numbers")
##    print("enter '-' to subtract numbers")
##    print("enter '*' to multiply numbers")
##    print("enter '/' to divide numbers")
##    print("enter 'mod' to get the reamains from division of numbers")
##    print("enter 'pow' to exponent up numbers")
##    print("enter 'div' to get the integer number of division of numbers")
##    print("enter 'quit' to quit program")

num1=float(input())
num2=float(input())
operation=input()
 
if operation=="+":
    print(num1+num2) 
elif operation=="-":
    print(num1-num2) 
elif operation=="*":
    print(num1*num2) 
elif operation=="/":
    if num2==0:
        print ("Деление на 0!")
    else:
        print(num1/num2) 
elif operation=="div":
    if num2==0:
        print ("Деление на 0!")
    else:
        print(num1//num2)
elif operation=="mod":
    if num2==0:
        print ("Деление на 0!")
    else:
        print(num1%num2)
elif operation=="pow":
    result=(num1**num2)
    print(result)
