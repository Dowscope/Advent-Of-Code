def makeArray(a1,a2):
    arr = []
    for i in range(a1, a2+1):
        arr.append(i)
    return arr

with open('data.txt', 'r') as file:
    lines = file.read()

file.close()

lines = lines.split('\n')
lines = list(filter(lambda x: x != "", lines))

seeds = lines.pop(0).split(':')[1].strip().split(' ')
lines.pop(0)

cats = []
cat_index = 0

print(seeds)
# print(lines)

cat = []
while len(lines) > 0:
    line = lines.pop(0)
    if ':' in line:
        cats.append(cat)
        cat = []
        continue
    cat.append(line)

    if len(lines) == 0:
        cats.append(cat)

# print(cats)

results = []

for seed in seeds:
    seed = int(seed)

    # print (f"------------- Seed {seed} ----------------")

    next_mapping = seed
    for cat in cats:
        for c in cat:
            parts = c.split(' ')
            
            src_start = int(parts[1])
            src_end = int(parts[1]) + int(parts[2]) - 1
            src = makeArray(src_start, src_end) 

            dst_start = int(parts[0])
            dst_end = int(parts[0]) + int(parts[2]) - 1
            dst = makeArray(dst_start, dst_end) 

            mapping = dict(zip(src, dst))

            del src
            del dst

            # print(cats)
            # print(parts)
            # print(mapping)
            # print(next_mapping)

            prev = next_mapping
            next_mapping = mapping.get(next_mapping, next_mapping)
            # print(next_mapping)

            if prev != next_mapping:
                break
    
    results.append( {'seed': seed, 'location': next_mapping})


print(results)
lowest = -1
for r in results:
    if lowest == -1 or lowest > r['location']:
        lowest = r['location']

print(f"Lowest is {lowest}")