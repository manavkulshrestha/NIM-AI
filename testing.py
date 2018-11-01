l = [3,1,3,4,1,4]

for e in l:
	print(format(e,f'0{max(l).bit_length()}b'))

print(f'BINARY TO INT: {int("101",2)}')