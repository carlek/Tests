

def solution(A):

    P = []
    t = 0
    for i in range(1, len(A)):
        t += A[i]
    P.append((A[0], t))

    if len(A) > 2:
        p = 0
        for i in range(1, len(A)-1):
            leftsum = P[i-1][0]
            rightsum = P[i-1][1]
            P.append((leftsum + A[i], rightsum - A[i]))

    diffs = []
    for i in range(len(P)):
        diffs.append(abs(P[i][0]-P[i][1]))

    return(min(diffs))


print(solution([3,1,2,4,3]))