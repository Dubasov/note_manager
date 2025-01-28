from config import *


def handle_error(error_type):
    """Функция обработки ошибок"""
    if error_type == "invalid_input":
        print("❌ Ошибка: Введены некорректные данные. Попробуйте снова.")
    elif error_type == 'command_error':
        print(MESSAGE_COMMAND_ERR)
    elif error_type == 'field_empty':
        print(MESSAGE_FIELD_EMPTY)
    elif error_type == "note_not_found":
        print("⚠️ Ошибка: Заметка не найдена. Проверьте правильность ввода.")
    elif error_type == "empty_list":
        print(MESSAGE_LST_EMPTY)
    else:
        print("⚠️ Неизвестная ошибка. Обратитесь в службу поддержки.")


# Пример использования
if __name__ == "__main__":
    handle_error("invalid_input")
    handle_error("note_not_found")
    handle_error("empty_list")
