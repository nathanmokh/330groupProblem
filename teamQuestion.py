import heapq
import random
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
    if middleCol[-1] and sum(A) % 2 == 0:
        #print('index of middle col: ' + str(half))
        return 0
    else:
        #check right side of column
        for i in range(half + 1, len(chart[0])):
            col = [item[i] for item in chart]
            if col[-1]:
                rightBound = i
                #print('rightBound: ' + str(i))
                break
        for i in reversed(range(0, half + 1)):
        #check left side of column
            col = [item[i] for item in chart]
            if col[-1]:
                leftBound = i
                #print('leftBound: ' + str(i))
                break
        return abs(leftBound - rightBound)


def q4a(A):
    chart = fillChart(A)
    return solve(chart, A)

def q4B(A):
    A = [-1*x for x in A]
    #print(A)
    heapq.heapify(A)

    while (len(A)>1):
        max = heapq.heappop(A)*-1
        secondMax = heapq.heappop(A)*-1
        diff = max-secondMax
        heapq.heappush(A,-diff)

    return A[0]*-1



#print(q4a([10, 7, 4, 4]))
#print(q4B([10, 8, 7, 6, 5]))

def getList(upperBound):
    ret = []
    for num in range(100):
        ret += [random.randint(1,upperBound)]
    return ret

def partC():
    bigList = []
    bounds = [1000, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11, 10**12] 
    for bound in bounds:
        bigList += [getList(bound)]
    for i in range(len(bigList)):
        print('Test ' + str(i) + ' on numbers 1 through ' + str(bounds[i]))
        print('Our algorithm: ' + str(q4a(bigList[i])))
        print('KK algorithm: ' + str(q4B(bigList[i])))
    


    
