from STAGE_5.interface import user_interface
from STAGE_5.data.file_handling import read_json


notes_lst = read_json('data_file')  # загрузка данных json

user_interface.interface(notes_lst) # запуск программы