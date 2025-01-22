from datetime import datetime

def validate_date(date_input):
    """Проверяет соответствие date_input формату день-месяц-год

    Если date_input соответствует формату, то возвращает дату в формате день-месяц-год (Str) иначе
    возвращает False
    """
    try:
        temp_issue_date = datetime.strptime(date_input, "%d-%m-%Y")
        return datetime.strftime(temp_issue_date, "%d-%m-%Y")  # дата в строку
    except ValueError:
        return False