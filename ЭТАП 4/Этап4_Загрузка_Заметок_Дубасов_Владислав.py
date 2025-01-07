import yaml


def load_notes_from_file(notes_file):
    """
    Функция принимает название файла.
    Открывает файл в режиме read и выводит содержимое при помощи функции display_notes.
    Обрабатывает ошибки сканера, чтения и доступа.
    """
    try:
        with open(f'{notes_file}.yaml', 'r', encoding='utf-8') as file:
            display = yaml.safe_load(file)
            print(display)
    except FileNotFoundError:
        print(r + f'\nОшибка чтения. Файла "{notes_file}.yaml" не существует!')
    except yaml.scanner.ScannerError:
        print(r + f'\nОшибка чтения файла. Файл "{notes_file}.yaml" повреждён!')
    except PermissionError:
        print(r + f'\nОшибка доступа. Программа не имеет доступа к файлу "{notes_file}"!')


load_notes_from_file('yamldata')
