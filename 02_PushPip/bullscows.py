from random import choice

lenght = 5
words = ["привет", "ропот", "котик", "крыса", "банка", "кепка"]
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
    while True:
        word = ask("Введите слово: ", words)
        res = bullscows(word, true_word)
        print(f"Быки: {res[0]}, Коровы: {res[1]}") # inform("Быки: {}, Коровы: {}", b, c)
        if res == (lenght, 0):
            print("УРА", word) 
            break


def ask(prompt: str, valid: list[str] = None) -> str:
    print(prompt)
    word = input()
    if valid != None:
        while word not in valid:
            print(prompt)
            word = input()
    return word


def inform():
    pass 

gameplay(ask, inform, words)
