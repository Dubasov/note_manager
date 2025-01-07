import yaml


def save_notes_to_file(notes, notes_file):
    """
    Принимает: список словарей (заметок) и 'название файла'.
    Создаёт файл если его не существует и перезаписывает в него список заметок.
    Если доступ к файлу отсутствует, то ловит ошибку PermissionError
    """
    try:
        with open(f"{notes_file}.yaml", "w", encoding='utf-8') as file:
            yaml.safe_dump(notes, file, sort_keys=False, allow_unicode=True)
            print('Файл перезаписан\n\n')
    except PermissionError:
        print(r + f'\nОшибка доступа. Программа не имеет доступа к файлу "{notes_file}.yaml"!')


notes_lst = [{'Note key yaml': 'Note value yaml'}]

save_notes_to_file(notes_lst, 'yamldata')

with open('yamldata.yaml', 'r', encoding='utf-8') as file:
    load = yaml.safe_load(file)

print(f'Тип данных: {type(load)}')
print(f'Содержимое: {load}')
