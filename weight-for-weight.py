string = '102 103 104 105 100 101 201'
weights = string.split()
fstring = ''
new = {1:['001']}
for w in weights:
	nsum = sum([int(i) for i in [*w]])
	if nsum not in new:
		new[nsum] = [w]	
	else:
		new[nsum].append(w)

for i in sorted(new.keys()):
	fstring += ''.join([j+' ' for j in sorted(new[i])])
	
print(new)

print(fstring)