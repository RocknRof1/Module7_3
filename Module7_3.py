file_name = 'fantom.txt'
with open(file_name, mode='r', encoding='utf-8') as file:
    white_list = file.read()
    print(white_list)

# оператор with автоматически закрывает файл.