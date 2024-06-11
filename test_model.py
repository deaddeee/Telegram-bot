import os
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import subprocess
import json

# Путь к папке с аудиофайлами .ogg
audio_folder = "audioOGG"

# Путь к вашей модели Vosk
model_path = "models/vosk/model"

# Создаем объект модели Vosk
model = Model(model_path)

# Функция для конвертации .ogg в .wav и распознавания аудиофайла
def recognize_audio(audio_file, recognizer):
    try:
        # Проверяем, существует ли уже .wav файл
        wav_file = os.path.splitext(audio_file)[0] + ".wav"
        if not os.path.exists(wav_file):
            # Конвертируем .ogg в .wav с помощью ffmpeg, если файл .wav еще не существует
            subprocess.run(["ffmpeg", "-i", audio_file, wav_file])
        
        # Открываем и обрабатываем .wav файл
        audio = AudioSegment.from_file(wav_file)
        audio = audio.set_channels(1).set_frame_rate(16000)  # Приведем к нужным параметрам
        data = audio.raw_data
        
        # Инициализируем распознаватель
        recognizer.AcceptWaveform(data)
        result = recognizer.FinalResult()
        
        # Добавим отладочный вывод
        print("Результат распознавания:", result)
        
        # Преобразуем результат в словарь
        result_dict = json.loads(result)
        
        # Получаем текст распознанной речи
        recognized_text = result_dict.get("text", "")
        
        return recognized_text
    except Exception as e:
        print(f"Ошибка обработки файла {audio_file}: {e}")
        return ""

# Получаем список всех аудиофайлов .ogg в папке и сортируем их
audio_files = sorted([filename for filename in os.listdir(audio_folder) if filename.endswith(".ogg")])

# Перебираем все аудиофайлы .ogg в порядке возрастания
all_results = []
for filename in audio_files:
    audio_file = os.path.join(audio_folder, filename)
    print(f"Обработка файла: {audio_file}")
    recognizer = KaldiRecognizer(model, 16000)
    recognized_text = recognize_audio(audio_file, recognizer)
    all_results.append(f"{filename}: {recognized_text}")

# Записываем результаты в текстовый файл
output_file = "результаты.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for result in all_results:
        f.write(result + "\n")

print("Результаты записаны в файл:", output_file)








