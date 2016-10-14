#программа проверяет, "счастливый" ли номер билета
#сумма первых трех цифр равна сумме оставшихся цифр

numbers=input()
    #"Введите шесть цифр билета: "))
 
num1=int(numbers[0])
num2=int(numbers[1])
num3=int(numbers[2])
num4=int(numbers[3])
num5=int(numbers[4])
num6=int(numbers[5])
        
if (num1+num2+num3)==(num4+num5+num6):
    print("Счастливый")
else:
    print ("Обычный")

