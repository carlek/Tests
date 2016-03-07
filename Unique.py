def solution(A):

    A.sort()
    prev = A[0]
    distinct = 1
    for i in range(1,len(A)):
        if A[i] != prev:
            distinct += 1
        prev = A[i]
    return distinct

s = [1,2,4,5,1,2,6,2,3]
print(solution(s))
s = [2, 1, 1, 2, 3, 1]
print(solution(s))
