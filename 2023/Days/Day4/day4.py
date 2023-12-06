with open('test.txt', 'r') as file:
    lines = file.readlines()

games_won = {}

for line in lines:
    line = line.replace('\n', '')

    card = line.split(':')[0].split(' ')[1]
    winners = line.split(':')[1].split(' | ')[0].strip().split(' ')
    picks = list(filter(lambda s: s != '', line.split(':')[1].split(' | ')[1].split(' ')))

    copies = 0
    if int(card) in games_won:
        copies = games_won[int(card)]

    matches = 0
    for i in range(copies + 1):
        for pick in picks:
            for winner in winners:
                if pick == winner:
                    matches += 1
        
        for m in range(int(card), matches + int(card) + 1):
            if m in games_won:
                games_won[m] += 1
            else:
                games_won[m] = 1

result = 0
for game in games_won:
    result += game

print(games_won)

print(result)