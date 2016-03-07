
def solution(S, P, Q):

    for i in range(len('ACGT')):
        S = S.replace('ACGT'[i], str(i+1))

    S = list(S)
    S = [int(i) for i in S]
    impact_factors = []
    for i in range(len(P)):
        p = P[i]
        q = Q[i]
        if p == q:
            impact_factors.append(S[p])
        else:
            impact_factors.append(min(S[p:q]))
    # write your code in Python 2.7
    return impact_factors

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))