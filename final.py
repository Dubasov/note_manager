#GRADE 1. ЭТАП 1. Задание 5.
    #Работа с объектами типа "дата"
import datetime

    #Библиотека для раскрашивания консоли
from colorama import init, Fore, Back, Style

    #Автосброс покраски строчек (сброс заданного цвета строчки для каждой команды print)
init(autoreset=True)

    #Объявляем словарь
note_dict = {}

    # Приветственное сообщение
print(Fore.GREEN +'* * ВАС ПРИВЕТСТВУЕТ МЕНЕДЖЕР ЗАМЕТОК 1.1.5 * *')

# _______ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ (ОЦП)_______
while True:
    # _______Командное меню_______
    print(Fore.CYAN +'\n- - * ВЫБЕРИТЕ СЛЕДУЮЩЕЕ ДЕЙСТВИЕ:'
          '\n Завершить работу - 0'
          '\n Вывести последнюю запись - 1'
          '\n Добавить заметку - 2'
          '\n Удалить заметку - 3\n')
        #Запрос команды от пользователя
    command_var = input(Fore.MAGENTA +'Введите команду: ')

    # _______Завершение программы (команда - 0)_______
    if command_var == '0':
        pass
        break

    # _______Отображение заметки (команда - 1)_______
    elif command_var == '1':
            # Проверка содержимого словаря (Если словарь пуст, то "Список заметок пуст", иначе цикл вывода данных
        if bool(note_dict) == False:
            print(Fore.RED +'\n(!) Список заметок пуст')
        else:
            for key, value in note_dict.items():
                print(f"{key}: {value}")
                # Консольная пауза (для удобства отображения)
            input(Fore.MAGENTA +'\nДля продолжения нажмите клавишу ENTER...')

    # _______Добавление заметки (команда - 2)_______
    elif command_var == '2':
            # Объявление списка заголовков
        note_dict['Заголовки'] = []
            #Запрос пользовательского ввода (ввод значений ключей)
        note_dict['Имя пользователя'] = input('Введите имя: ')
            # Цикл для запроса пользовательского ввода трёх заголовков
        for item in range(3):
            title = input(f'Введите заголовок заметки {item + 1}: ')
            note_dict['Заголовки'].append(title)
        note_dict['Описание'] = input('Введите описание: ')
            # Цикл статуса заметки
        while True:
            print(Fore.CYAN +'Выберите статус заметки: '
                  'Активна - 1; '
                  'Отложена - 2; '
                  'Выполнена - 3.')
            status_command = input(Fore.MAGENTA +'Введите команду: ')
            if status_command == '1':
                note_dict['Статус'] = 'Активна'
                break
            elif status_command == '2':
                note_dict['Статус'] = 'Отложена'
                break
            elif status_command == '3':
                note_dict['Статус'] = 'Выполнена'
                break
            else:
                print(Fore.RED +'\n(!) Такой команды не существует! Пожалуйста, введите доступную команду.')
                continue
            # Получение текущей даты
        note_dict['Дата создания'] = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m")
            # Получение даты завершения заметки и проверка пользовательского ввода
        while True:
            try:
                temp_issue_date = datetime.datetime.strptime(
                    input(Fore.MAGENTA +'Ввведите дату завершения (день-месяц-год): '), "%d-%m-%Y")
                issue_date = datetime.datetime.strftime(temp_issue_date, "%d-%m")
                note_dict['Дата завершения'] = issue_date
                break
            except ValueError:
                print(Fore.RED +'\n(!) Пожалуйста, соблюдайте формат даты **день-месяц-год**')
                continue
            # Сообщение об успешном действии
        print(Fore.GREEN +'\nЗаметка успешно сохранена!')
            # Консольная пауза
        input(Fore.MAGENTA +'\nДля продолжения нажмите клавишу ENTER...')

    # _______Удаление заметки (команда - 3)_______
    elif command_var == '3':
        if bool(note_dict) != False:
            note_dict.clear()
            print(Fore.GREEN +'Заметка удалена')
                # Консольная пауза
            input(Fore.MAGENTA +'\nДля продолжения нажмите клавишу ENTER...')
        else:
            print(Fore.RED +'(!) Список заметок пуст')

        # ОЦП. Обработка пользовательского ввода (введённой команды не существует)
    else:
        print(Fore.RED +'\n(!) Такой команды не существует! Пожалуйста, введите доступную команду.')
        continue