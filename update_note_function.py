# GRADE 1. ЭТАП 3. Задание 2.

from create_note_function import *

init(autoreset=True)  # Авто сброс покраски строчек

# Укрощение colorama цветов
r = Fore.RED
m = Fore.MAGENTA
c = Fore.CYAN
g = Fore.GREEN
lg = Fore.LIGHTGREEN_EX
y = Fore.YELLOW


# ФУНКЦИЯ РЕДАКТИРОВАНИЯ
def update_note(add_note_dict):
    print(y + '\n................РЕДАКТИРОВАНИЕ ЗАМЕТКИ................')

    # МЕНЮ КОМАНД ДЛЯ ВЫБОРА ПОЛЯ ДЛЯ РЕДАКТИРОВАНИЯ
    while True:
        print(c + '\nВыберите поле для редактирования '
                  '\n○ Имя пользователя   — 1'
                  '\n○ Темы               — 2'
                  '\n○ Описание           — 3'
                  '\n○ Статус             — 4'
                  '\n○ Дата завершения    — 5'
                  '\n○ Изменить все поля  — 6')

        # Ввод команды
        key_changer = input(m + '\nВведите команду: ')

        # ______КОМАНДА 1_________Изменение имени пользователя
        if key_changer == '1':
            add_name(add_note_dict)  # ф-ия добавления имени

            accept_action = input('Для подтверждения действия введите д: ')  # подтверждение
            if accept_action == 'д':
                print(lg + '\nИЗМЕНЕНИЯ СОХРАНЕНЫ')
                return add_note_dict  # возвращает словарь с изменённым полем
            else:
                print(r + '\nДЕЙСТВИЕ ОТМЕНЕНО')
                break  # возвращает none

        # ______КОМАНДА 2_________Изменение тем
        elif key_changer == '2':
            add_titles(add_note_dict)

            accept_action = input('Для подтверждения действия введите д: ')
            if accept_action == 'д':
                print(lg + '\nИЗМЕНЕНИЯ СОХРАНЕНЫ')
                return add_note_dict
            else:
                print(r + '\nДЕЙСТВИЕ ОТМЕНЕНО')
                break

        # ______КОМАНДА 3_________Изменение описания
        elif key_changer == '3':
            add_description(add_note_dict)

            accept_action = input('Для подтверждения действия введите д: ')
            if accept_action == 'д':
                print(lg + '\nИЗМЕНЕНИЯ СОХРАНЕНЫ')
                return add_note_dict
            else:
                print(r + '\nДЕЙСТВИЕ ОТМЕНЕНО')
                break

        # ______КОМАНДА 4_________Изменение статуса
        elif key_changer == '4':
            add_status(add_note_dict)

            accept_action = input('Для подтверждения действия введите д: ')
            if accept_action == 'д':
                print(lg + '\nИЗМЕНЕНИЯ СОХРАНЕНЫ')
                return add_note_dict
            else:
                print(r + '\nДЕЙСТВИЕ ОТМЕНЕНО')
                break

        # ______КОМАНДА 5_________Изменение даты
        elif key_changer == '5':
            date_mechanism(add_note_dict)

            accept_action = input('Для подтверждения действия введите д: ')
            if accept_action == 'д':
                print(lg + '\nИЗМЕНЕНИЯ СОХРАНЕНЫ')
                return add_note_dict
            else:
                print(r + '\nДЕЙСТВИЕ ОТМЕНЕНО')
                break

        # ______КОМАНДА 6_________Изменение всех полей
        elif key_changer == '6':
            add_name(add_note_dict)
            add_titles(add_note_dict)
            add_description(add_note_dict)
            date_mechanism(add_note_dict)
            add_status(add_note_dict)

            accept_action = input('Для подтверждения действия введите д: ')
            if accept_action == 'д':
                print(lg + '\nИЗМЕНЕНИЯ СОХРАНЕНЫ')
                return add_note_dict
            else:
                print(r + '\nДЕЙСТВИЕ ОТМЕНЕНО')
                break
        else:
            print(r + '\n(!) Такой команды не существует! Пожалуйста, введите доступную команду.')
            continue


add_note_dict = {'Имя пользователя': 'Елена',
                 'Темы': ['Тестовый заголовок 1 в заметке Елены'],
                 'Описание': 'Тестовое описание-2 в заметке Елены',
                 'Создана': '15-12-2024',
                 'Дата завершения': '10-01-2025'}

if '__main__' == __name__:
    print(g + '* * ВАС ПРИВЕТСТВУЕТ Ф-ИЯ РЕДАКТИРОВАНИЯ ЗАМЕТКИ 1.3.2 * *')
    if update_note(add_note_dict):
        print(add_note_dict)
