cats = []
cafes = []
maxim = 0

while True:
    bar = input()
    if bar == 'MEOW':
        break
    else:
        cafe = bar.split()[0]
        cat = int(bar.split()[1])
        cafes.append(cafe)
        cats.append(cat)

maxim = max(cats)
print(cafes.index(cats(maxim)))