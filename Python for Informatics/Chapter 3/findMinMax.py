largest = None
smallest = None

while True:
	num = raw_input("Enter a number: ")
	if num == "done" :
		break
	
	try:
		val=float(num)
	except:
		print 'Invalid input'
		continue
	
	if smallest is None:
		smallest = float(num)
		
	if largest is None:
		largest = float(num)
	
	if float(num) > largest:
		largest = float(num)
		
	if float(num) < smallest:
		smallest = float(num)
		
print "Maximum is", largest
print "Minimum is", smallest