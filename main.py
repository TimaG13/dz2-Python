user_input = int(input("Введіть 5-ти значне число: "))

# Розділяємо число на окремі цифри
digit5 = user_input % 10
digit4 = (user_input // 10) % 10
digit3 = (user_input // 100) % 10
digit2 = (user_input // 1000) % 10
digit1 = (user_input // 10000) % 10

#Перевертаємо число і виводимо результат
res_num = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1
print("Результат:", res_num)