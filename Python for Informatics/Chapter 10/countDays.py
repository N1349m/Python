name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

timecount = dict()

for line in handle:
	if line.startswith('From '):
		wordsplit = line.split()
		time = wordsplit[5].split(':')
		timecount[time[0]] = timecount.get(time[0],0)+1

timesort = timecount.items()
timesort.sort()

for k,v in timesort:
	print k,v