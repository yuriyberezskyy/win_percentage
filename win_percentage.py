def win_percentage(wins, losses):
    return round(wins ** 2 / (wins ** 2 + losses ** 2) * 100)


print(win_percentage(10, 0))
