
## Завершение Этапа 7
### STAGE_7 /
- |── [**color_output.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_7/color_output.py)
- |── [**config.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_7/config.py)
- |── [**console_menu.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_7/console_menu.py)
- |── [**error_handling_ui.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_7/error_handling_ui.py)
- |── [**filters_menu.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_7/filters_menu.py)
- |── [**pagination.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_7/pagination.py)
### Описание
Этап разработки включает создание функций меню  программы, цветного вывода статусов, пагинации и управления ошибками
- **color_output.py** (содержит функции для цветного вывода в консоли)
- **console_menu.py**	(содержит функцию консольного меню)
- **error_handling_ui.py**	(функция для управления ошибками)
- **filters_menu.py**	(функция для фильтрации заметок по ключевому слову, статусу или дате)
- **pagination.py**	(постраничное отображение заметок)

--- 
## Завершение Этапа 6
### STAGE_6 /
- |── [**database/**](https://github.com/Dubasov/note_manager/tree/master/STAGE_6/database)
- ||────── [__init__.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/database/__init__.py)
- ||────── [note_operations.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/database/note_operations.py)
- ||────── [setup_database.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/database/setup_database.py)
- |── [**tests/**](https://github.com/Dubasov/note_manager/tree/master/STAGE_6/tests)
- ||────── [test_note_database.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/tests/test_note_database.py)
- |── [**S6_utils/**](https://github.com/Dubasov/note_manager/tree/master/STAGE_6/S6_utils)
- ||────── [__init__.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/S6_utils/__init__.py)
- ||────── [console_resume.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/S6_utils/console_resume.py)
- ||────── [display_notes.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/S6_utils/display_notes.py)
- ||────── [validate_date.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/S6_utils/validate_date.py)
- ||────── [validate_input.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/S6_utils/validate_input.py)
- ||────── [validate_status.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_6/S6_utils/validate_status.py)
- |── [config.py](https://github.com/Dubasov/note_manager/tree/master/STAGE_6/config.py)
- |── [**main.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_6/main.py)

### Описание
Этап разработки включает создание функций для работы с БД sqlite3
- **database/** (содержит функции для создания, редактирования, удаления, чтения, поиска и фильтрации заметок в БД sqlite3)
- **tests/**	(содержит функции тестирования)
- **S6_utils/**	(содержит вспомогательные функции для валидации и отображения данных)
--- 
## Завершение Этапа 5
### STAGE_5 /
- |── [**data/**](https://github.com/Dubasov/note_manager/tree/master/STAGE_5/data)
- ||────── [file_handling.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/data/file_handling.py)
- |── [**interface/**](https://github.com/Dubasov/note_manager/tree/master/STAGE_5/interface)
- ||────── [display_notes.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/interface/display_notes.py)
- ||────── [search_notes.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/interface/search_notes.py)
- ||────── [user_interface.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/interface/user_interface.py)
- |── [**tests/**](https://github.com/Dubasov/note_manager/tree/master/STAGE_5/tests)
- ||────── [tests.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/tests/tests.py)
- |── [**utils/**](https://github.com/Dubasov/note_manager/tree/master/STAGE_5/utils)
- ||────── [console_resume.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/utils/console_resume.py)
- ||────── [generate_unique_id.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/utils/generate_unique_id.py)
- ||────── [validate_date.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/utils/validate_date.py)
- ||────── [validate_input.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/utils/validate_input.py)
- ||────── [validate_status.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_5/utils/validate_status.py)
- |── [config.py](https://github.com/Dubasov/note_manager/tree/master/STAGE_5/config.py)
- |── [**main.py**](https://github.com/Dubasov/note_manager/tree/master/STAGE_5/main.py)

### Описание
Этап разработки включает создание структуры проекта Note_manager. Структура данного проекта включает пакеты: 
- **date/** (содержит функции для создания, редактирования, удаления, чтения и записи файлов)
- **interface/** (содержит функции отображения, поиска и пользовательского меню)
- **tests/**	(содержит функции тестирования)
- **utils/**	(содержит вспомогательные функции для валидации и генерации данных)
--- 
## Завершение Этапа 4
### STAGE_4/
- |────── [scaner-err.yaml](https://github.com/Dubasov/note_manager/blob/master/STAGE_4/scaner-err.yaml)
- |────── [Этап4_JSON_Формат_Дубасов_Владислав.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_4/Этап4_JSON_Формат_Дубасов_Владислав.py)
- |────── [Этап4_Добавление_Данных_Дубасов_Владислав.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_4/Этап4_Добавление_Данных_Дубасов_Владислав.py)
- |────── [Этап4_Загрузка_Заметок_Дубасов_Владислав.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_4/Этап4_Загрузка_Заметок_Дубасов_Владислав.py)
- |────── [Этап4_Обработка_Ошибок_Дубасов_Владислав.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_4/Этап4_Обработка_Ошибок_Дубасов_Владислав.py)
- |────── [Этап4_Сохранение_Заметок_Дубасов_Владислав.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_4/Этап4_Сохранение_Заметок_Дубасов_Владислав.py)
### Описание
- **scaner-err.yaml** (Повреждённый файл для обработки ошибок)
- **Этап4_JSON_Формат_Дубасов_Владислав.py** (Перезапись файла JSON)
- **Этап4_Добавление_Данных_Дубасов_Владислав.py** (Дозапись в файл YAML)
- **Этап4_Загрузка_Заметок_Дубасов_Владислав.py** (Загрузка данных из файла YAML)
- **Этап4_Обработка_Ошибок_Дубасов_Владислав.py** (Обработка ошибок при чтении файлов YAML)
- **Этап4_Сохранение_Заметок_Дубасов_Владислав.py** (Перезапись файла YAML)
--- 
## Завершение Этапа 3
### STAGE_3/
- |────── [create_note_function.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_3/create_note_function.py)
- |────── [update_note_function.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_3/update_note_function.py)
- |────── [display_notes_function.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_3/display_notes_function.py)
- |────── [search_notes_function.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_3/search_notes_function.py)
- |────── [menu.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_3/menu.py)

### Описание
- **create_note_function.py** (Функции добавления заметки)
- **update_note_function.py** (Функция редактирования заметки на базе функций создания заметки)
- **display_notes_function.py** (Функция отрисовки заметок)
- **search_notes_function.py** (Функции поиска заметок)
- **menu.py** (Функция меню программы, которая позволяет вызывать все реализованные на данном этапе функции)
--- 
## Завершение Этапа 2
### STAGE_2/
- |────── [add_titles_loop.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_2/add_titles_loop.py)
- |────── [update_status.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_2/update_status.py)
- |────── [check_deadline.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_2/check_deadline.py)
- |────── [multiple_notes.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_2/multiple_notes.py)
- |────── [delete_note.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_2/delete_note.py)

### Описание
- **add_titles_loop.py** (Создание списка пользовательских тем в заметке)
- **update_status.py** (Выбор из списка или ввод пользовательского статуса заметки)
- **check_deadline.py** (Проверка срока истечения заметки)
- **multiple_notes.py** (Создание неограниченного количества пользовательских заметок)
- **delete_note.py** (Позволяет удалять заметки по поиску имени, теме или номеру заметки)
--- 
## Завершение Этапа 1
### STAGE_1/
- |────── [greetings.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_1/greetings.py)
- |────── [date_changer.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_1/date_changer.py)
- |────── [add_input.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_1/add_input.py)
- |────── [add_list.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_1/add_list.py)
- |────── [final.py](https://github.com/Dubasov/note_manager/blob/master/STAGE_1/final.py)

### Описание
- **greetings.py** (Программа содержит основные переменные)
- **date_changer.py** (Создание пользовательской заметки с маской для ввода даты завершения и выбором статуса записи)
- **add_input.py** (Создание пользовательской заметки, содержащей несколько заголовков с маской для ввода даты завершения и выбором статуса записи)
- **add_list.py** (Создание пользовательской заметки, содержащей несколько заголовков с применением цикла for с маской для ввода даты завершения и выбором статуса записи)
- **final.py** (Создание пользовательской заметки на основании dictionary, содержащей несколько заголовков с применением цикла for с маской для ввода даты завершения и выбором статуса записи)
