def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")     # Первым делом проверяем деление на 3 и 5 вместе
        elif i % 3 == 0:
            print("Fizz")         # Потом проверяем только на 3
        elif i % 5 == 0:
            print("Buzz")         # Далее проверяем только на 5
        else:
            print(i)              # Иначе выводим само число

# Тестируем функцию:
fizz_buzz(30)