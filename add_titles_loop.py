# GRADE 1. ЭТАП 1. Задание 5.
# Работа с объектами типа "дата"
import datetime

# Библиотека для раскрашивания консоли
from colorama import init, Fore, Back, Style

# Авто сброс покраски строчек (сброс заданного цвета строчки для каждой команды print)
init(autoreset=True)

# Укрощение (извращение) colorama's цветов, дико извиняюсь
r = Fore.RED
m = Fore.MAGENTA
c = Fore.CYAN
g = Fore.GREEN
lg = Fore.LIGHTGREEN_EX
y = Fore.YELLOW

# ФУНКЦИЯ ПОСТ-ПАУЗЫ
def console_pause():
    """Создаёт поле ввода в консоли.
    Представляет собой разделитель действий во время выполнения программы"""
    command_pause = input(g + '\nУспешно. Для продолжения работы нажмите клавишу ENTER...')

# ФУНКЦИЯ ПРОВЕРКИ ПОЛЬЗОВАТЕЛЬСКОГО ВВОДА
def correct_input(a):
    """Обрабатывает пользовательский ввод на наличие только пробелов либо пустого ввода

    Принимает: введенное пользователем значение
    Возвращает: True или False"""
    return a.isspace() == False and a != ''

# ФУНКЦИЯ ДОБАВЛЕНИЯ ТЕМ
def add_titles_loop():
    """Представляет собой цикл добавления нескольких тем с обработкой ввода

    Требует для работы: словарь add_note_dict;
    Содержит: ключ словаря 'Темы'.
    Механизм: запрашивает бесконечный цикл ввода тем с проверкой на уникальность.
    Не позволяет вводить только пробелы. Завершает цикл при пустом вводе
    """
    print(c + 'Программа запрашивает несколько уникальных заголовков,'
              ' для прерывания операции оставьте поле пустым.')
    add_note_dict['Темы'] = []
    title_ticker = 1  # Переменная счётчик введённых заголовков
    while True:
        title = input(m + f'Введите тему заметки {title_ticker}: ')
        # Условие только пробелы или пустой ввод
        if title != '':
            if title.isspace() == True:
                print(r + '(!) Тема заметки не может содержать только пробелы')
            else:
                # Условие поиска совпадений
                if add_note_dict['Темы'].count(title):
                    print(r + '(!)Такая тема заметки уже существует. '
                              'Пожалуйста, введите уникальную тему или завершите ввод.')
                    continue
                    # Добавление заголовков в список ключа
                else:
                    add_note_dict['Темы'].append(title)
                    title_ticker = title_ticker + 1
            # Условие выхода из цикла, если список содержит хотя бы одну тему, а ввод пуст
        elif title == '' and len(add_note_dict['Темы']) > 0:
            title_ticker = 1
            break
        else:
            print(r + '(!) Должен быть хотя бы он заголовок')

# ФУНКЦИЯ ОТРИСОВКИ ЗАМЕТОК
def print_notes_loop():
    """Предназначения для читаемого вывода списка заметок и срока до дедлайна.

    Требует для работы: библиотеку import datetime и colorama;
    перебор списка словарей (обязательно с функцией enumerate), где каждый словарь помещается в переменную note;
    ключи 'Имя пользователя', 'Темы', 'Описание', 'Создана', 'Дата завершения', 'Статус'
    Содержит: ключи 'Создана' 'Дата завершения', цикл перебора словаря note
    Механизм: функция получает дату создания и дату завершения из итерации цикла перебора
    БД (на данный момент это список словарей) и сравнивает их, получая объект timedelta,
    а затем выводит его результат, при помощи блока условий. Другой цикл функции
    перебирает ключи и значения словаря с выводом через функцию print
    """
    # Получение временной (temp) текущей даты для вычисления объекта timedelta
    temp_created_date = datetime.datetime.strptime(note['Создана'], "%d-%m-%Y")
    temp_issue_date = datetime.datetime.strptime(note['Дата завершения'], "%d-%m-%Y")
    # Визуальный разделитель
    print('⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯')
    # Счетчик итератора, расположенного вне функции
    print(y + f'Заметка {iteration + 1}')
    # Перебор словаря note
    for key, value in note.items():
        # Соответствие типу данных list (для корректного вывода тем)
        if type(value) == list:
            print('▶ Тема: ', *value, sep=' |✎')
        # Вывод всех остальных типов данных
        else:
            print(f'▶ {key}: {value}')

        # Сравнение (temp) текущей даты и даты завершения deadline_var представляет собой объект timedelta
    if temp_created_date < temp_issue_date:
        deadline_var = temp_issue_date - temp_created_date
        print(lg + "↪ Осталось {} дней".format(deadline_var.days))
    elif temp_created_date > temp_issue_date:
        deadline_var = temp_created_date - temp_issue_date
        print(r + "↪ Просрочено на {} дней".format(deadline_var.days))
    else:
        print(r + '↪ Истекает сегодня')


# Список словарей с предустановленными заметками
notes_lst = [{'Имя пользователя': 'Влад',
              'Темы': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
              'Описание': 'Тестовое описание-1 в заметке влада',
              'Создана': '15-12-2024',
              'Дата завершения': '15-12-2024'
              }
             ]

print(g + '* * ВАС ПРИВЕТСТВУЕТ МЕНЕДЖЕР ЗАМЕТОК 1.2.1 * *')

print(y+'\nДля проверки задания отредактируйте темы предустановленной заметки и выведите список заметок')
# ___________ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ____________
while True:
    # Командное меню
    print(c + '\nВыберите команду, соответствующую пункту меню:'
              '\n○ Показать список заметок — 2 '
              '\n○ Редактировать заметку   — 3 '
              '\n○ Завершить работу        — 5')

    # Пользовательский ввод команды
    command_add = input(m + '\nВведите команду: ')

    # ____КОМАНДА 2______Показать список заметок
    if command_add == '2':
        print(y + '\nОТОБРАЖЕНИЕ СПИСКА ЗАМЕТОК')
        if len(notes_lst) == 0:
            print(r + '\nСписок заметок пуст')
        for iteration, note in enumerate(notes_lst):
            print_notes_loop()
        console_pause()

    # ____КОМАНДА 3______Редактирование заметки
    elif command_add == '3':
        print(y + '\nРЕДАКТИРОВАНИЕ ЗАМЕТКИ')
        # ЦИКЛ ПОИСКА ЗАМЕТКИ
        while True:
            try:
                print(c + f'\nВведите номер заметки для внесения изменений. '
                          f'Доступные значения команды от 1 до {len(notes_lst)}')
                # Пользовательский ввод номера заметки для редактирования
                note_change_command = int(input(m + '\nВведите команду: '))
                # Проверка ввода
                if note_change_command < 1:
                    print(r + '(!) Такой заметки не существует')
                    continue
                elif note_change_command > len(notes_lst):
                    print(r + '(!) Такой заметки не существует')
                    continue
            except ValueError:
                print(r + '(!) Команда должна быть целым числом')
                continue
            else:

                # Извлечение заметки из списка по индексу (индекс = тикер - 1)
                add_note_dict = notes_lst.pop(note_change_command - 1)
                break
        # МЕНЮ КОМАНД ДЛЯ ВЫБОРА ПОЛЯ ДЛЯ РЕДАКТИРОВАНИЯ
        while True:
            print(c + '\nВыберите поле для редактирования. '
                      '\n○ Темы — 2')
            # Ввод команды
            key_changer = input(m + '\nВведите команду: ')
            # ______Команда 2_________Изменение тем
            if key_changer == '2':
                add_titles_loop()
                notes_lst.insert((note_change_command - 1), add_note_dict)
                print(lg + '\nИЗМЕНЕНИЯ СОХРАНЕНЫ')
                console_pause()
                break
            else:
                print(r + '\n(!) Такой команды не существует! Пожалуйста, введите доступную команду.')
                continue

    # ____КОМАНДА 5______Выход из программы
    elif command_add == '5':
        pass
        break
    else:
        print(r + '\n(!) Такой команды не существует! Пожалуйста, введите доступную команду.')
        continue
