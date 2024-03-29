with open('data.txt', 'r') as file:
    lines = file.readlines()

games_won = {}

for line in lines:
    line = line.replace('\n', '')

    card = int(line.split(':')[0].split(' ')[-1])
    winners = line.split(':')[1].split(' | ')[0].strip().split(' ')
    picks = list(filter(lambda s: s != '', line.split(':')[1].split(' | ')[1].split(' ')))

    # print(f"line:{line}")
    # print(f"card:{card}")
    # print(f"winners:{winners}")
    # print(f"picks:{picks}")

    copies = 0
    if card in games_won:
        copies = games_won[card]

    matches = 0
    for pick in picks:
        for winner in winners:
            if pick == winner:
                matches += 1

    if card in games_won:
        games_won[card] += 1
    else:
        games_won[card] = 1
    # print(f"Card: {card} | Won so far: {games_won[card]}")

    if matches > 0:
        for m in range(card + 1, matches + card + 1):
            if m in games_won:
                games_won[m] += 1
            else:
                games_won[m] = 1
            # print(f"og win - card: {m} | {games_won[m]}")

    # print(f"{copies} copies of Card {card}")
    for i in range(copies):
        for m in range(card + 1, matches + card + 1):
            if m in games_won:
                games_won[m] += 1
            else:
                games_won[m] = 1
            # print(f"card: {m} | {games_won[m]}")
    # print("----------------------------")

result = 0
for game in games_won:
    # print(game)
    result += int(games_won[game])

print(games_won)

print(result)