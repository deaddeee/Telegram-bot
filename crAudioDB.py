from gtts import gTTS
import os

def text_to_speech(file_path):
    # Открытие текстового файла и прочтение строки
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Создание директории для сохранения аудиофайлов
    output_dir = "DB"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Обработка каждой строки и сохранение аудиофайла
    for i, line in enumerate(lines):
        line = line.strip()
        if line:  # Если строка не пустая
            tts = gTTS(text=line, lang='ru')
            file_name = os.path.join(output_dir, f"line_{i+1}.ogg")
            tts.save(file_name)
            print(f"Saved {file_name}")

# Путь к текстовому файлу
text_file_path = "train.txt"
text_to_speech(text_file_path)