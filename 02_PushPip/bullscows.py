lenght = 5

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

