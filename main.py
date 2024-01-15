x = int(input("Число:"))
y = int(input("Число:"))

i = j = 0
while i < y:
    j = 0
    while j < x:
        if j <= int(x/2):
            if i <= j:
                print(f'[{i},{j}]', end=' ')
            else:
                print(f'[{i},{j}]', end=' ')

        else:
            if i + j <= y-1:
                print(f'[{i},{j}]', end='')
            else:
                print(f'[{i},{j}]', end='')
        j += 1
        print()
        i += 1