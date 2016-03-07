
def solution(A):
    count = {}
    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    print(count)
    for c in range(1, len(count)+1):
        if c not in count:
            return c






print(solution([1, 3, 6, 4, 1, 2]))
