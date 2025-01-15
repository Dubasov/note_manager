import json

def save_notes_json(notes, json_file):
    """
    Принимает список заметок и название файла.
    Создаёт файл json если его не существует и перезаписывает в него список заметок.
    """
    try:
        with open(f'{json_file}.json', 'w', encoding='utf8') as file:
            json.dump(notes_lst, file, indent=4, ensure_ascii=False)
    except PermissionError:
        print(r + f'\nОшибка доступа. Программа не имеет доступа к файлу "{json_file}"!')



notes_lst = [{'Note key json': 'Note value json'}]

save_notes_json(notes_lst,'jsondata')

with open('jsondata.json', 'r', encoding='utf-8') as file:
    load = json.load(file)


print(f'Содержимое: {load}')