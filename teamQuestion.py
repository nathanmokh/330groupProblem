def getArray(seq):
    ret = [[False for x in range(sum(seq) + 1)] for y in range(len(seq))] 
    return ret

def q1(A):
    chart = getArray(A)
    for r in range(len(chart)):
        for c in range(len(chart[0])):
            if chart[r][c]:
                continue
            elif c == 0:
                chart[r][c] = True
            elif c == A[r]:
                chart[r][c] = True
            elif c > A[r]:
                continue
            elif r != 0 and chart[r-1][c]:
                chart[r][c] = True
                
    return chart
