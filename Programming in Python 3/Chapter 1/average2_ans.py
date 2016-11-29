lst = []
count = 0
numsum = 0
highest = None
lowest = None

while True:
    line = input("enter a number or Enter to finish: ")
    if not line:
        print("numbers: ",lst)
        print("count =", count," sum = ", numsum," lowest = ", lowest,"highest = ",
        highest," mean = ", numsum/count)

        lstsort = []
        total = count
        while count > 0:
            lowest = None
            for num in lst:
                if lowest is None or num < lowest:
                    lowest = num
            lst.remove(lowest)
            lstsort.append(lowest)
            count -= 1

        if int(total/2) - total/2 == 0:
            index1 = int((total - 1) / 2 )
            index2 = int((total + 1) / 2 )
            print("median = ",(lstsort[index1]+lstsort[index2])/2)
        else:
            index = int(total / 2 )
            print("median = ",lstsort[index])
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
