import yaml

def append_notes_to_file(notes, notes_file):
    """
    Принимает список словарей (заметок) и название файла.
    Создаёт файл yaml если его не существует и дозаписывает в него список заметок.
    Если доступ к файлу отсутствует, то ловит ошибку PermissionError
    """
    try:
        with open(f"{notes_file}.yaml", "a", encoding='utf-8') as file:
            yaml.safe_dump(notes, file, sort_keys=False, allow_unicode=True)
    except PermissionError:
        print(r + f'\nОшибка доступа. Программа не имеет доступа к файлу "{notes_file}.yaml"!')


notes_lst = [{'Note key yaml': 'Note value yaml'}]


append_notes_to_file(notes_lst, 'yamldata-append')

with open('yamldata-append.yaml', 'r', encoding='utf-8') as file:
    load = yaml.safe_load(file)


print(f'Содержимое: {load}')