while True:
    print("options:")
    print("enter 'add' to add numbers")
    print("enter 'subtract' to subtract numbers")
    print("enter 'multiply' to multiply numbers")
    print("enter 'divide' to divide numbers")
    print("enter 'quit' to quit program")
    user_input=input(":")
    if user_input=='quit':
        break
    elif user_input=="add":
        num1=float(input("enter number 1: "))
        num2=float(input("enter number 2: "))
        result=str(num1+num2)
        print("Result:", result) 
    elif user_input=="subtract":
        num1=float(input("enter number 1: "))
        num2=float(input("enter number 2: "))
        result=str(num1-num2)
        print("Result:", result) 
    elif user_input=="multiply":
        num1=float(input("enter number 1: "))
        num2=float(input("enter number 2: "))
        result=str(num1*num2)
        print("Result:", result) 
    elif user_input=="divide":
        num1=float(input("enter number 1: "))
        num2=float(input("enter number 2: "))
        result=str(num1/num2)
        print("Result:", result) 
    else:
        print("unknown input")
