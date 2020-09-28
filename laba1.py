import csv

count_sentence = 0
count_all = 0
count_space = 0
count_word = 0
count_punctuation = 0
punctuation = [',', '.', ':', ';', '(', ')', '?', '!', '"', "'"]
isPunctuation = False
isWord = False
isSentence = False

with open('steam_description_data.csv',  encoding='latin-1') as file:
    for stroka in file:
        for symbol in stroka:                               # Посимвольно обрабатыем файл
            if symbol != ' ' and isWord == False:           # Подсчет слов, где с помощью isWord проверяем находится ли
                count_word += 1                             # наш символ внутри слова или снаружи
                isWord = True
            else:
                if symbol == ' ':
                    isWord = False

            if symbol != '.' and isSentence == False:       # Подсчет предложений, работает аналогично подсчету слов
                count_sentence += 1
                isSentence = True
            else:
                if symbol == '.':
                    isSentence = False

            if symbol == ' ':                               # Подсчет пробелов
                count_space += 1

            for i in punctuation:                           # Проверка является ли symbol знаком препинания с помощью цикла, который
                if symbol == i:                             # проходится по списку знаков препинания
                    isPunctuation = True
            if isPunctuation == True:
                count_punctuation += 1                      # Подсчет знаокв препинания
                isPunctuation = False

            count_all += 1                                  # Подсчет всех знаков

print('Количество символов всего -', count_all)
print('Количество символов без пробелов -', count_all-count_space)
print('Количество символов без знаков препинания -', count_all-count_punctuation)
print('Количество слов -', count_word)
print('Количество предложений -', count_sentence)
