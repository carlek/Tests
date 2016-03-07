# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def binary_string(N):
    n = N
    bs = ''
    while n:
        bs = ('1' if n%2 else '0') + bs
        n //= 2
    return(bs)

def solution(N):
    n = N
    curr_count = 0
    high_count = 0
    start_counting = False
    while n:
        if n % 2:
            break
        n //= 2

    while n:
        if n % 2 == 0:
            curr_count += 1
            if curr_count > high_count:
                high_count = curr_count
        else:
            curr_count = 0
        n //= 2
    return high_count

print(binary_string(1041))
print(solution(1041))

print(binary_string(272))
print(solution(272))
