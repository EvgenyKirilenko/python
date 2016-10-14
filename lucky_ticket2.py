#программа проверяет, "счастливый" ли номер билета
#сумма первых трех цифр равна сумме оставшихся цифр

numbers=(input("Введите шесть цифр билета: "))
if (int(numbers[0])+(int(numbers[1]))+(int(numbers[2])))==(int(numbers[3]))+(int(numbers[4]))+(int(numbers[5])):
    print("Счастливый")
else:
    print ("Обычный")
