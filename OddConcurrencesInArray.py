from collections import Counter

def solution(A):
    odd_man = None
    C = sorted(A)
    prev = None
    counter = 0
    for c in C:
        if c == prev:
            counter += 1
        else:
            if counter == 1:
                odd_man = prev
            counter = 1
        prev = c
    return odd_man

A = [9, 3, 9, 3, 9, 7, 9, 7]
print(solution(A))

