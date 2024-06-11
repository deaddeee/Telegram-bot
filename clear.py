# Открываем файл для чтения
with open('результаты.txt', 'r') as file:
    lines = file.readlines()

# Открываем файл для записи
with open('recognized_speech.txt', 'w') as file:
    # Проходим по каждой строке
    for line in lines:
        # Разбиваем строку по ":", выбираем вторую часть и удаляем начальные и конечные пробелы
        cleaned_line = line.split(":")[1].strip()
        # Записываем очищенную строку в файл
        file.write(cleaned_line + '\n')
