
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rownum = len(numbers)
for i in range(rownum):
    cnum = len(numbers[i])
    rowsum = 0
    for j in range(rownum):
       # print (numbers[i][j], end = " ")
        rowsum =+ numbers[i][j]
print (numbers[i][j], end = " ")

cnum = len(numbers[0])
for i in range(cnum):
    colsum = 0
    for j in range(rownum):
        colsum =+ numbers[j][i]
    
for i in range(rownum):
    rowsum = sum(numbers[i])
print (numbers[j][i], end = " ")