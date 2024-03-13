import os

def merge_files(file_list, output_file):
    # Проверяем существование файлов
    for filename in file_list:
        if not os.path.exists(filename):
            print(f"Файл {filename} не существует.")
            return
    
    # Создаем список кортежей (содержимое файла, имя файла)
    files_data = [(open(filename, encoding="utf-8").read(), filename) for filename in file_list]
    
    # Сортируем список по количеству строк в файле
    files_data.sort(key=lambda x: x[0].count('\n'))
    
    # Открываем результирующий файл для записи
    with open(output_file, 'w', encoding="utf-8") as out_file:
        # Записываем информацию о каждом файле и его содержимое
        for data, filename in files_data:
            line_count = data.count('\n') + 1
            # Записываем информацию о файле
            out_file.write(f'{filename}\n{line_count}\n')
            # Записываем содержимое файла с символом новой строки после каждой строки
            out_file.write(data)
            out_file.write('\n')  # Добавляем символ новой строки

file_list = ['1.txt', '2.txt', '3.txt']
output_file = 'merged_file.txt'

merge_files(file_list, output_file)