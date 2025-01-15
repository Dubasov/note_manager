from datetime import datetime

def validate_date(date_input):
    try:
        temp_issue_date = datetime.strptime(date_input, "%d-%m-%Y")
        issue_date = datetime.strftime(temp_issue_date, "%d-%m-%Y")  # дата в строку
        return issue_date
    except ValueError:
        return False