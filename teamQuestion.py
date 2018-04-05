def getArray(seq):
    ret = [[False for x in range(sum(seq) + 1)] for y in range(len(seq))] 
    return ret


def fillChart(A):
    chart = getArray(A)
    chart[0][0] = True
    chart[0][A[0]] = True
    total = sum(A)
    for r in range(1, len(chart)):
        for c in range(len(chart[0])):
            if chart[r - 1][c]:
                chart[r][c] = True
                if A[r] + c <= total:
                    chart[r][A[r] + c] = True
    return chart
            
            
            
def printArray(A):
    for each in A:
        print(each)
        


def solve(chart, A):
    half = sum(A) // 2
    #get target middle column
    middleCol = [item[half] for item in chart]
    #if the column contains a true, then residue is 0
    if middleCol[-1]:
        return 0
    else:
        #check right side of column
        for i in range(half + 1, len(chart[0])):
            col = [item[i] for item in chart]
            if col[-1]:
                rightBound = i
                break
        for i in reversed(range(0, half)):
        #check left side of column
            col = [item[i] for item in chart]
            if col[-1]:
                leftBound = i
                break
        return abs(leftBound - rightBound)


def q4a(A):
    return solve(fillChart(A), A)

def q4B(A):
    A.sort()
    nonZero = True
    while (nonZero):
        diff = A[len(A)-1] - A[len(A)-2]
        A[len(A)-1] = diff
        A[len(A)-2] = 0
        A.sort()
        #print(A)
        if (A[len(A)-2]==0):
            nonZero = False

    return A[len(A)-1]


print(q4a([10, 7, 4, 4]))
print(q4B([10, 8, 7, 6, 5]))
