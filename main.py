x = 4
y = 4

i = j = 0
wall = x
while i < x:
    j = 0
    while j < y:
        if i >= j:
            print(f'[{i},{j}]', end=' ')
        else:
            print(f'    ', end=' ')
        j += 1
    print()
    i += 1


    i = j = 0
    while i < x:
        j = 0
        while j < y:
            if j <= wall-i-1:
                print(f'[{i},{j}]', end=' ')
            else:
                print(f'     ', end=' ')
            j += 1
        print()
        i += 1