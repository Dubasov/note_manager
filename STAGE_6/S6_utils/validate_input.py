
# ФУНКЦИЯ ПРОВЕРКИ ПОЛЬЗОВАТЕЛЬСКОГО ВВОДА
def validate_input(input_value):
    """Проверяет значение аргумента input_value

    Если input_value пустое или содержит только пробелы, возвращает False иначе True."""
    return input_value.strip() != ''
if __name__=='__main__':
    print('False: ', validate_input(" "))
    print('True: ', validate_input(" w"))