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
            return display

    except FileNotFoundError:
        print(f'\nОшибка чтения. Файла "{notes_file}.yaml" не существует!')
    except yaml.scanner.ScannerError:
        print(f'\nОшибка чтения файла. Файл "{notes_file}.yaml" повреждён!')
    except PermissionError:
        print(f'\nОшибка доступа. Программа не имеет доступа к файлу "{notes_file}"!')



print(load_notes_from_file('yamldata'))