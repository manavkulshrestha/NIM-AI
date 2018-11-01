import random

piles = [7,5,3,1]
pile_thresh = 10

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

if(input('Play with default configuration?-\n\tpile = [7,5,3,1]\n\tpile threshold = 10\n\tyou go first\n(y/n): ') != 'y'):
	# AI_is_P1 = (input('do you want to go first? (y/n):') != 'y')
	pile_thresh = int(input('Input pile threshold (how large a pile can be) [1,100]: '))#no upper bound, but recommended
	if(pile_thresh < 1):
		pile_thresh = 1

	pile_count = int(input('Input number of piles to play with [2,10]: '))#no upper bound, but recommended
	if pile_count < 2:
		pile_count = 2

	if input('Do you want to go first? (y/n):') != 'y':#AI is Player 1
		while(True):
			piles = [random.randint(1,pile_thresh) for i in range(pile_count)]
			if get_nim_sum(piles) != 0:
				break
		print_piles(piles)
		print('\nAI is playing...\n')
		piles = make_move(piles)
	else:
		piles = make_move([random.randint(1,pile_thresh) for i in range(pile_count)])

while(True):
    print_piles(piles)

    max_index = len(piles)-1
    index = int(input((f'\nInput index of pile [0,{max_index}]: ')))
    if index < 0:
        index = 0
    elif index > max_index:
        index = max_index

    remove = int(input(f'Input objects to remove [1{","+str(piles[index]) if piles[index] != 1 else ""}]: '))
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

