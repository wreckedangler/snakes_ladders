import random

p1 = 1
draws = 0
games = 0
goal = 1000000
snakes = 0
ladders = 0

while p1 != 100:
    p1 += random.randint(1, 6)
    draws += 1

    # Ladders


    if p1 == 8:
        p1 = 26
        ladders += 1
    if p1 == 19:
        p1 = 38
        ladders += 1
    if p1 == 12:
        p1 = 73
        ladders += 1
    if p1 == 28:
        p1 = 53
        ladders += 1
    if p1 == 36:
        p1 = 57
        ladders += 1
    if p1 == 43:
        p1 = 77
        ladders += 1
    if p1 == 50:
        p1 = 91
        ladders += 1
    if p1 == 54:
        p1 = 86
        ladders += 1
    if p1 == 62:
        p1 = 96
        ladders += 1
    if p1 == 66:
        p1 = 87
        ladders += 1
    if p1 == 80:
        p1 = 99
        ladders += 1

    # Snakes

    if p1 == 44:
        p1 = 22
        snakes += 1
    if p1 == 46:
        p1 = 15
        snakes += 1
    if p1 == 48:
        p1 = 9
        snakes += 1
    if p1 == 52:
        p1 = 11
        snakes += 1
    if p1 == 59:
        p1 = 18
        snakes += 1
    if p1 == 64:
        p1 = 22
        snakes += 1
    if p1 == 68:
        p1 = 2
        snakes += 1
    if p1 == 69:
        p1 = 33
        snakes += 1
    if p1 == 83:
        p1 = 22
        snakes += 1
    if p1 == 92:
        p1 = 51
        snakes += 1
    if p1 == 95:
        p1 = 37
        snakes += 1
    if p1 == 98:
        p1 = 13
        snakes += 1

    # end

    if p1 >= 100:
        games += 1
        p1 = 1

    if games == goal:
        snakes_per_game = snakes / goal
        ladders_per_game = ladders / goal
        draws_per_game = draws / goal

        print(f"""Snakes and Ladders
        - Total games = {games}
        - Snakes per game = {snakes_per_game}
        - Ladders per game = {ladders_per_game}
        - Draws per game = {draws_per_game}""")

        break

