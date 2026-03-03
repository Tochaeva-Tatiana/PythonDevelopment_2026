from random import choice
import urllib.request
import argparse

words = ["папка", "ропот", "котик", "крыса", "банка", "кепка", "книга"]

def bullscows(version: str, mystery: str):
    bull = cow = 0
    bull_l = []
    for i in range(args.lenght):
        if version[i] == mystery[i]:
            bull += 1
            bull_l.append(mystery[i])
        elif (version[i] in mystery) and (version[i] not in bull_l):
            cow +=1
    return (bull, cow)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    true_word = choice(words)
    count = 0
    while True:
        count += 1
        word = ask("Введите слово: ", words)
        res = bullscows(word, true_word)
        inform("Быки: {}, Коровы: {}", res[0], res[1])
        if res == (args.lenght, 0):
            ask(f"Поздравляю! Количество попыток: {count}")
            break
        


def ask(prompt: str, valid: list[str] = None) -> str:
    print(prompt)
    if valid != None:
        word = input()
        while word not in valid:
            print(prompt)
            word = input()
        return word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

parser = argparse.ArgumentParser()
parser.add_argument("dictionary", default=None)
parser.add_argument("lenght", default=5, type=int)
args = parser.parse_args()

try:
    with open(args.dictionary, 'r', encoding='utf-8') as f:
        words = []
        for line in f:
            if line.strip() and len(line.strip()) == args.lenght:
                words += [line.strip()]
except FileNotFoundError:
    try:
        with urllib.request.urlopen(args.dictionary) as response:
            # Читаем данные, декодируем в utf-8 (или другую кодировку, если нужно)
            data = response.read().decode('utf-8')
            # Разбиваем на строки, убираем пустые и пробельные
            words = [line.strip() for line in data.splitlines() if line.strip() and len(line.strip()) == args.lenght]
    except:
        print("Не удалось открыть")

# if type(args.dictionary)
gameplay(ask, inform, words)
