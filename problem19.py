def sundayTheFirst(start, end):
    daysHash = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
        16: [],
        17: [],
        18: [],
        19: [],
        20: [],
        21: [],
        22: [],
        23: [],
        24: [],
        25: [],
        26: [],
        27: [],
        28: [],
        29: [],
        30: [],
        31: []
    }
    day = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        0: 'Sunday'
    }
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    month = 1
    i = 1
    j = 1
    while month != 13:
        daysHash[i].append(day[i % 7])
        i += 1
        if i == months[month]:
            daysHash[i].append(day[i % 7])
            month += 1
            j = i
            i = 1


    sundayFirsts = 0
    for i in daysHash[1]:
        if i == 'Sunday':
            sundayFirsts += 1
    return sundayFirsts

print(sundayTheFirst(1901, 2001))
