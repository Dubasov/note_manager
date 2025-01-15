# GRADE 1. ЭТАП 3. Задание 1.

import datetime  # Работа с датами
from colorama import init, Fore  # Библиотека для раскрашивания консоли

init(autoreset=True)  # Авто сброс покраски строчек

# Укрощение colorama цветов
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
    input(g + '\nУспешно. Для продолжения работы нажмите клавишу ENTER...')


# ФУНКЦИЯ ПРОВЕРКИ ПОЛЬЗОВАТЕЛЬСКОГО ВВОДА
def correct_input(a):
    """Обрабатывает пользовательский ввод на наличие только пробелов либо пустого ввода

    Принимает: введенное пользователем значение
    Возвращает: True или False"""
    return a.isspace() == False and a != ''


# ФУНКЦИЯ ДОБАВЛЕНИЯ ИЛИ РЕДАКТИРВОАНИЯ ИМЕНИ ПОЛЬЗОВАТЕЛЯ
def add_name(add_note_dict):
    """Представляет собой цикл добавления имени пользователя с обработкой ввода

    Требует для работы: словарь add_note_dict;
    Содержит: ключ словаря 'Имя пользователя'
    """
    while True:
        add_note_dict['Имя пользователя'] = input(m + '\nВведите имя: ')
        # Проверка пользовательского ввода при помощи функции correct_input
        if correct_input(add_note_dict['Имя пользователя']):
            break
        else:
            print(r + '(Ошибка ввода) Имя пользователя не может быть пустым. Пожалуйста, повторите ввод')
            continue
    print(lg + '\nИмя пользователя сохранено.\n')


# ФУНКЦИЯ ДОБАВЛЕНИЯ ИЛИ РЕДАКТИРОВАНИЯ ТЕМ
def add_titles(add_note_dict):
    print(c + 'Программа запрашивает несколько уникальных заголовков,'
              ' для прерывания операции оставьте поле пустым.')
    add_note_dict['Темы'] = []
    title_ticker = 1  # Переменная счётчик введённых заголовков
    while True:
        title = input(m + f'Введите тему {title_ticker}: ')
        if correct_input(title):  # Ф-ия проверки пробелы либо пустой ввод
            if title.lower() in (item.lower() for item in add_note_dict['Темы']):  # Поиск совпадений
                print(r + '(Ошибка ввода) Такая тема заметки уже существует.')
                continue
            else:
                add_note_dict['Темы'].append(title)  # Добавление заголовков в список ключа
                title_ticker = title_ticker + 1
        elif title.isspace():  # Если только пробел\ы
            print(r + '(Ошибка ввода) Тема заметки не может содержать только пробелы.')
            continue
        elif title == '' and len(add_note_dict['Темы']) > 0:
            break
        else:
            print(r + '(Ошибка ввода) Должна быть хотя бы одна тема.')
    print(lg + '\nСписок тем сохранён.\n')


# ФУНКЦИЯ ДОБАВЛЕНИЯ ИЛИ РЕДАКТИРОВАНИЯ ОПИСАНИЯ ЗАМЕТКИ
def add_description(add_note_dict):
    while True:
        add_note_dict['Описание'] = input(m + 'Введите описание: ')
        if correct_input(add_note_dict['Описание']):
            break
        else:
            print(r + '(!) Описание не может быть пустым. Пожалуйста, повторите ввод')
            continue
    print(lg + '\nОписание сохранено.\n')


# ФУНКЦИЯ ДОБАВЛЕНИЯ ПОЛЬЗОВАТЕЛЬСКОГО СТАТУСА
def user_status(add_note_dict):
    while True:
        add_note_dict['Статус'] = input(m + '\nВведите пользовательский статус: ')
        if correct_input(add_note_dict['Статус']):
            break
        else:
            print(r + '(Ошибка ввода) Статус не может быть пустым! Попробуйте заново.')
            continue


# ФУНКЦИЯ ВЫБОРА ИЛИ РЕДАКТИРОВАНИЯ СТАТУСА
def add_status(add_note_dict):
    while True:
        print(c + 'Выберите статус заметки. Для ввода пользовательского статуса используйте команду 4: '
                  '\n○ Активна          — 1; '
                  '\n○ Отложена         — 2; '
                  '\n○ Выполнена        — 3; '
                  '\n○ Ввести статус    — 4.')

        status_command = input(m + '\nВведите команду: ')  # пользовательский ввод

        # _____КОМАНДА 1_________добавление статуса "Активна"
        if status_command == '1':
            add_note_dict['Статус'] = 'Активна'
            break

        # _____КОМАНДА 2_________добавление статуса "Отложена"
        elif status_command == '2':
            add_note_dict['Статус'] = 'Отложена'
            break

        # _____КОМАНДА 3_________добавление статуса "Выполнена"
        elif status_command == '3':
            add_note_dict['Статус'] = 'Выполнена'
            break

        # _____КОМАНДА 4_________добавление пользовательского статуса
        elif status_command == '4':
            user_status(add_note_dict)
            break

        else:
            print(r + '(Ошибка ввода) Такой команды не существует! Пожалуйста, введите доступную команду.')
            continue
    print(lg + f'\nСтатус «{add_note_dict.get('Статус')}» сохранен\n')


# ФУНКЦИЯ СУММОНА И ВВОДА ДАТ
def date_mechanism(add_note_dict):
    # Получение текущей даты
    add_note_dict['Создана'] = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%Y")
    # Получение даты завершения заметки и проверка пользовательского ввода
    while True:
        try:
            temp_issue_date = datetime.datetime.strptime(
                input(m + 'Введите дату завершения (день-месяц-год): '), "%d-%m-%Y")

            issue_date = datetime.datetime.strftime(temp_issue_date, "%d-%m-%Y")
            add_note_dict['Дата завершения'] = issue_date
            break
        except ValueError:
            print(r + '(Ошибка ввода) Пожалуйста, соблюдайте формат даты || день-месяц-год ||')
            continue


# ФУНКЦИЯ СОЗДАНИЯ
def create_note():
    add_note_dict = {}  # Объявление словаря внутри функции

    print(y + '\n................ДОБАВЛЕНИЕ НОВОЙ ЗАМЕТКИ................')

    add_name(add_note_dict)  # Ф-ия добавления имени
    add_titles(add_note_dict)  # Ф-ия добавления заголовков
    add_description(add_note_dict)  # Ф-ия добавления описания
    add_status(add_note_dict)  # Ф-ия статуса
    date_mechanism(add_note_dict)  # Ф-ия работы с датами

    while True:
        accept_action = input('Для подтверждения действия введите д: ')  # подтверждение
        if accept_action == 'д':
            print(lg + '\nЗАМЕТКА СОХРАНЕНА')
            return add_note_dict  # Возвращает словарь
        else:
            print(r + '\nДЕЙСТВИЕ ОТМЕНЕНО')
            break  # возвращает None


# Добавление заметки

if '__main__' == __name__:
    print(g + '* * ВАС ПРИВЕТСТВУЕТ Ф-ИЯ ДОБАВЛЕНИЯ ЗАМЕТКИ 1.3.1 * *')
    print(create_note())
