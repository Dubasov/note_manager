#GRADE 1. ЭТАП 1. Задание 4.
    #Работа с объектами типа "дата"
import datetime

    #Библиотека для раскрашивания консоли
from colorama import init, Fore, Back, Style

    #Автосброс покраски строчек
init(autoreset=True)

    # Приветственное сообщение
print(Fore.GREEN +'* * ВАС ПРИВЕТСТВУЕТ МЕНЕДЖЕР ЗАМЕТОК 1.1.4 * *')

    # _______ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ (ОЦП)_______
while True:
        # Командное меню
    print(Fore.CYAN +'\n- - * ВЫБЕРИТЕ СЛЕДУЮЩЕЕ ДЕЙСТВИЕ:'
          '\n Завершить работу - 0'
          '\n Вывести последнюю запись - 1'
          '\n Добавить заметку - 2\n')

    command_var = input(Fore.MAGENTA +'Введите команду: ')

    # _______Завершение программы (команда - 0)_______
    if command_var == '0':
        pass
        break

    # _______Отображение заметки (команда - 1)_______
    elif command_var == '1':
        while True:
            try:
                print('\nИмя пользователя: ', username)
                print('Заголовки: ', titles_lst)
                print('Описание: ', content)
                print('Статус: ', status)
                print('Дата создания: ', created_date)
                print('Дата завершения: ', datetime.datetime.strftime(issue_date, "%d-%m"))
                    # Консольная пауза
                input(Fore.MAGENTA +'\nДля продолжения нажмите клавишу ENTER...')
                break
            except NameError:
                print(Fore.RED +'\n(!) Список заметок пуст')
                break
        continue

    # _______Добавление заметки (команда - 2)_______
    elif command_var == '2':
            #Объявление пустого списка
        titles_lst = []
            #Запрос пользовательского ввода
        username = input('Введите имя: ')
        for item in range(3):
            title = input(f'Введите заголовок заметки {item + 1}: ')
            titles_lst.append(title)
        content = input('Введите описание: ')
            # Цикл статуса заметки
        while True:
            print(Fore.CYAN +'Выберите статус заметки: '
                  'Активна - 1; '
                  'Отложена - 2; '
                  'Выполнена - 3.')
            status_command = input(Fore.MAGENTA +'Введите команду: ')
            if status_command == '1':
                status = 'Активна'
                break
            elif status_command == '2':
                status = 'Отложена'
                break
            elif status_command == '3':
                status = 'Выполнена'
                break
            else:
                print(Fore.RED +'\n(!) Такой команды не существует! Пожалуйста, введите доступную команду.')
                continue
            # Получение текущей даты
        created_date = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m")
            # Получение даты завершения заметки и проверка пользовательского ввода
        while True:
            try:
                temp_issue_date = input(Fore.MAGENTA +'Ввведите дату завершения (день-месяц-год): ')
                issue_date = datetime.datetime.strptime(temp_issue_date, "%d-%m-%Y")
                break
            except ValueError:
                print(Fore.RED +'\n(!) Пожалуйста, соблюдайте формат даты **день-месяц-год**')
                continue
            # Сообщение об успешном действии
        print(Fore.GREEN +'\nЗаметка успешно сохранена!')
            # Консольная пауза
        input(Fore.MAGENTA +'\nДля продолжения нажмите клавишу ENTER...')

        # ОЦП. Обработка пользовательского ввода (введённой команды не существует)
    else:
        print(Fore.RED +'\n(!) Такой команды не существует! Пожалуйста, введите доступную команду.')
        continue
