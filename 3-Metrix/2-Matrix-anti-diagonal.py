N  = int(input("Enter the integer size of the square matrix"))

def AntiDiagonal(N):
    A = [[10*j+i+10 for i in range(N)] for j in range(N)]
    for i in A:
        print(i)
    print("< ---------------------------------------------------- > ")
    diagonals = []
    for i in range(1, 2*N):
        if i  <= N:
            num_ele = i
            row = 0
            col = i-1
        if i > N:
            num_ele = 2*N - i
            col = N-1
            row = i-N
        ints = []
        for i in range(num_ele):
            ints.append(A[row+i][col-i])
        diagonals.append(ints)
    for i in diagonals:
        print(i)
                
AntiDiagonal(N)