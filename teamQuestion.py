def getArray(seq):
    ret = [[False for x in range(sum(seq) + 1)] for y in range(len(seq))] 
    return ret


def q1AltAgain(A):
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
        


