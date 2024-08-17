# Самостоятельная работа по уроку "Рекурсия"

# Объявление функции get_multiplied_digits с параметром number
def get_multiplied_digits(number):
    # Преобразование параметра number в строковый параметр
    str_number = str(number)
    # Присвоение first целочисленного значения первого символа переменной str_number
    first = int(str_number[0])
    # условия достижинея последнего символа в переменной str_number
    if len(str_number) <= 1:
        # когда достигли последнего символа
        return first
    # когда не достигли последнего символа
    else:
        # вывод результата перемножения чисел переменной (0 в теле числа пропускается)
        return first * get_multiplied_digits(int(str_number[1:]))


# Исходный код:
result = get_multiplied_digits(40203)

# Вывод на консоль:
print(result)
