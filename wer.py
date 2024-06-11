import nltk

def calculate_wer(ground_truth, recognized):
    # Разбиение исходного текста и распознанных предложений на слова
    gt_words = ground_truth.split()
    rec_words = recognized.split()
    
    # Инициализация матрицы расстояний
    d = [[0] * (len(rec_words) + 1) for _ in range(len(gt_words) + 1)]
    
    # Заполнение матрицы расстояний
    for i in range(len(gt_words) + 1):
        for j in range(len(rec_words) + 1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            else:
                substitution_cost = 0 if gt_words[i - 1] == rec_words[j - 1] else 1
                d[i][j] = min(d[i - 1][j] + 1,      # Удаление
                              d[i][j - 1] + 1,      # Вставка
                              d[i - 1][j - 1] + substitution_cost)  # Замена
    
    # Вывод матрицы расстояний
    print("Матрица расстояний:")
    for row in d:
        print(row)
    
    # Итоговое значение WER
    wer = d[len(gt_words)][len(rec_words)] / len(gt_words)
    
    return wer * 100

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().strip()

# Имя файла с исходным текстом
ground_truth_file = "train.txt"
# Имя файла с распознанной речью
recognized_file = "recognized_speech.txt"
print("Чтение файла с исходным текстом...")
ground_truth = read_file(ground_truth_file)
print("Файл с исходным текстом прочитан.")

print("Чтение файла с распознанной речью...")
recognized = read_file(recognized_file)
print("Файл с распознанной речью прочитан.")

print("Вычисление WER...")
wer = calculate_wer(ground_truth, recognized)
print("WER:", wer)

