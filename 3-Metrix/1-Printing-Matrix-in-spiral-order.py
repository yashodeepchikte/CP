## Printing matrix in spiral order
# given N = 5
# output = 
# 1  2  3  4  5
#16...........6
#15...........7
#14...........8
#13 12  11 10 9

row = int(input("Enter the number of rows in the  matrix"))
col = int(input("Enter the number of columns in the matrix"))
def printSpiral(row, col):
    A = [[0]*col for i in range(row)]
    left = 0
    right = col-1
    top = 0
    bottom = row-1
    direction = 0
    num = 1
    while top <= bottom and left <= right:
        if direction == 0:      #-------------> moving to the right
            for i in range(left, right+1):
                A[top][i] = num
                num +=1
            top += 1
            direction = 1
        if direction == 1:  #-------------------. Moving down
            for i in range(top, bottom+1):
                A[i][right] = num
                num += 1
            right-=1
            direction = 2
        if direction == 2:
            for i in list(range(left, right+1))[::-1]:
                A[bottom][i] = num
                num += 1
            bottom -= 1
            direction = 3
        if direction == 3:
            for i in list(range(top, bottom+1))[::-1]:
                A[i][left] = num
                num += 1
            left += 1
            direction = 0
    for i in A:
        print(i)
printSpiral(row, col)