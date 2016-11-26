lst = []
count = 0
numsum = 0
highest = None
lowest = None

while True:
    line = input("enter a number or Enter to finish: ")
    if not line:
        print("count =", count," sum = ", numsum," lowest = ", lowest,"highest = ",
        highest," mean = ", numsum/count)
        break
    try:
        num = int(line)
    except ValueError:
        print("input not int")
    lst += [num]
    count += 1
    numsum += num
    if highest is None or num > highest:
        highest = num
    if lowest is None or num < lowest:
        lowest = num
