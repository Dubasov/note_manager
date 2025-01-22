def validate_status(dct):
    statuses = ['Активна', 'Отложена', 'Выполнена']
    return dct.get('status') in statuses
