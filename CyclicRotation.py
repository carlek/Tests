
def solution(S, K):
    A = list(S)
    B = A[:]
    for i in range(len(A)):
        if i + K >= len(A):
            B[i + K - len(A)] = A[i]
        else:
            B[i+K] = A[i]
    return ''.join(B)

def reverse(S):
    R = ''
    for i in range(len(S), -1, -1):
        R += S[i]
    return


print(solution('abc', 2))
print(solution('abcd', 1))
print(solution('abcde', 4))
print(solution('abcdef', 3))

