def validate_status(add_note_dict):
    statuses = ['Активна', 'Отложена', 'Выполнена']
    if add_note_dict.get('Статус') in statuses:
        return True
    else:
        return False