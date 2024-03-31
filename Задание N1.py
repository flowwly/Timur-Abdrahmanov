num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
    
print(f"Вы ввели числа: {num1} и {num2}")
    
print("Какое действие выполнить?")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
    
choice = int(input(">"))
    
if choice == 1:
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Ошибка: деление на ноль невозможно.")
else:
    print("Неверный выбор операции.")
