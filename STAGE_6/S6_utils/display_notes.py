from datetime import datetime  # Работа с датами
from STAGE_6.config import *

# ФУНКЦИЯ ОТРИСОВКИ ЗАМЕТОК ПРИ ПОИСКЕ
def notes_display(note, note_id):
    print(MESSAGE_DISP_SEP)  # >> ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    print(y + f'Заметка: {note_id}')
    for key, value in note.items():  # Перебор словаря note
        if isinstance(value, list):  # Если type = list
            print('▶ Тема: '.ljust(22, ' '), '; '.join(value))  # список в строку
        else:
            if key == 'ID':
                pass
            elif key == 'username':
                print(f'▶ Имя пользователя: '.ljust(22, ' '), f'{value}')
            elif key == 'content':
                print(f'▶ Описание: '.ljust(22, ' '), f'{value}')
            elif key == 'status':
                print(f'▶ Статус: '.ljust(22, ' '), f'{value}')
            elif key == 'created_date':
                print(f'▶ Создана: '.ljust(22, ' '), f'{value}')
            elif key == 'issue_date':
                print(f'▶ Дата завершения: '.ljust(22, ' '), f'{value}')


    # ДЕДЛАЙН
    temp_created_date = datetime.now()
    temp_issue_date = datetime.strptime(note['issue_date'], "%d-%m-%Y")

    if temp_created_date < temp_issue_date:  # Блок сравнения дат
        if note.get('status') != 'Выполнена':
            deadline_var = temp_issue_date - temp_created_date
            print(MESSAGE_DISP_BEF.format(deadline_var.days))  # >> Осталось {} дней
    elif temp_created_date > temp_issue_date:
        if note.get('status') != 'Выполнена':
            deadline_var = temp_created_date - temp_issue_date
            print(MESSAGE_DISP_AFT.format(deadline_var.days))  # >> Просрочено на {} дней
    else:
        if note.get('status') != 'Выполнена':
            print(MESSAGE_DISP_TOD)  # >> Истекает сегодня


if '__main__' == __name__:
    # Список словарей с предустановленными заметками
    notes_lst = [{'Имя пользователя': 'Влад',
                  'Темы': ['Тестовый заголовок 1 в заметке Влада', 'Тестовый заголовок 2 в заметке Влада'],
                  'Описание': 'Тестовое описание-1 в заметке влада',
                  'Статус': 'Отложена',
                  'Создана': '15-12-2024',
                  'Дата завершения': '15-12-2024'
                  },
                 {'Имя пользователя': 'Елена',
                  'Темы': ['Тестовый заголовок 1 в заметке Елены'],
                  'Описание': 'Тестовое описание-2 в заметке Елены',
                  'Статус': 'Выполнена',
                  'Создана': '15-12-2024',
                  'Дата завершения': '10-01-2025'
                  }
                 ]

    print(g + '* * ВАС ПРИВЕТСТВУЕТ Ф-ИЯ ОТРИСОВКИ ЗАМЕТКИ 1.3.3 * *')
    searched_notes = []
    for iteration, note in enumerate(notes_lst):
        note_id = iteration + 1
        searched_notes.append(note_id)
        notes_display(note, note_id)

