fname = raw_input("Enter file name: ")
fh = open(fname)
readtext = fh.read()
readtext2 = readtext.strip()

print readtext.upper()