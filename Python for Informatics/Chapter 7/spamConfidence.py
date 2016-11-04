filename = raw_input('Enter file name: ')
file = open(filename,'r')

# file = open('mbox-short.txt')

total = 0;
count = 0;
for line in file:
	if line.startswith("X-DSPAM-Confidence:"):	
		start = line.find('0')
		end = line.find('\n')
		number = line[start:end+1]
		total = total + float(number)
		count = count + 1
print 'Average spam confidence:', total/count