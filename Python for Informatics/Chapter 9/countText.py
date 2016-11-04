name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

countr = dict()

for line in handle:
	if line.startswith('From '):
		splt = line.split()
		address = splt[1]
		countr[address] = countr.get(address,0)+1

big_contributor = None
for key in countr: 
	if big_contributor is None or countr.get(key,0) > countr.get(big_contributor,0): big_contributor = key

print big_contributor, countr.get(big_contributor,0)