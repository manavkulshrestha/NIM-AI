piles = [7,5,3,1]

def get_nim_sum(l):
    nim_sum = 0
    for e in l:
        nim_sum ^= e
    return nim_sum

def make_move(l):
    new_pile = l.copy()
    for i, column in enumerate(new_pile):
        for diff in range(1,column+1):
            new_pile[i] -= 1
            if get_nim_sum(new_pile) == 0:
                if 0 in new_pile:
                    new_pile.remove(0)
                return new_pile
        new_pile[i] = column
    return None

def print_piles(l):
    print(''.join(['indexes:\t','\t'.join(f'[{str(e)}]' for e in range(len(l))),'\npiles:\t\t','\t'.join(f' {str(e)}' for e in l)]))

while(True):
    print_piles(piles)

    max_index = len(piles)-1
    index = int(input((f'\ninput index of pile [0,{max_index}]: ')))
    if index < 0:
        index = 0
    elif index > max_index:
        index = max_index

    remove = int(input(f'input objects to remove [1{","+str(piles[index]) if piles[index] != 1 else ""}]: '))
    if remove < 1:
        remove = 1
    elif remove > piles[index]:
        remove = piles[index]

    piles[index] -= remove
    if 0 in piles:
        piles.remove(0)
    print()
    print_piles(piles)
    piles = make_move(piles)
    if(piles == []):
        break
    print('\nAI is playing...\n')

print('\nAI has won!')

