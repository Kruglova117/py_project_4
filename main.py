x = 4
y = 4

i = j = 0

while i < x:
    j = 0
    while j < y:
        print(f'[{i},{j}]', end=' ')
        j += 1
    print()
    i += 1