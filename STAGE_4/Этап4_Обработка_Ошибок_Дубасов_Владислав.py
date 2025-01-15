import yaml
from STAGE_3.display_notes_function import *


def load_notes_from_file(notes_file):
    """
    Функция принимает название файла.
    Открывает файл в режиме read и выводит содержимое при помощи функции display_notes.
    Обрабатывает ошибки сканера, чтения и доступа.
    """
    try:
        with open(f'{notes_file}.yaml', 'r', encoding='utf-8') as file:
            display_notes(yaml.safe_load(file))  # демонстрация при помощи функции из 3 этапа
    except FileNotFoundError:
        print(r + f'\nОшибка чтения. Файла "{notes_file}.yaml" не существует!')
    except yaml.scanner.ScannerError:
        print(r + f'\nОшибка чтения файла. Файл "{notes_file}.yaml" повреждён!')
    except ValueError:
        print(r + f'\nОшибка чтения файла. Файл "{notes_file}.yaml" повреждён!')
    except PermissionError:
        print(r + f'\nОшибка доступа. Программа не имеет доступа к файлу "{notes_file}"!')



print('Файла не существует:')
load_notes_from_file('notfound')

print('\nНет доступа к файлу:')
load_notes_from_file('permission-err')

print('\nОшибка чтения файла:')
load_notes_from_file('scaner-err')