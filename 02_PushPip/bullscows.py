from random import choice

lenght = 5
words = ["папка", "ропот", "котик", "крыса", "банка", "кепка"]
def bullscows(version: str, mystery: str):
    bull = cow = 0
    bull_l = []
    for i in range(lenght):
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
        print("Быки: {}, Коровы: {}", res[0], res[1]) # inform("Быки: {}, Коровы: {}", b, c)
        if res == (lenght, 0):
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
    pass

gameplay(ask, inform, words)
