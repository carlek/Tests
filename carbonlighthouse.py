def create_dict(T):
    # create dictionary with {key:value, ...}
    # as {(temp,n):index, (temp,n):index,...}
    # where n is from 0-N (to force uniqueness)
    res = {}
    n = 0
    for (i,t) in enumerate(T):
        res[(t,n)] = i
        n += 1
    return res

from collections import OrderedDict
def sort_temperatures(D):
    # sort dictionary based on key (temperature)
    res = OrderedDict()
    for tuple in sorted(D.keys()):
        res[tuple] = D[tuple]
    return res

def solution(T):
    # create dictionary
    temperature_dict = create_dict(T)

    # sort dictionary
    sorted_temperature_dict = sort_temperatures(temperature_dict)

    # keep track of anchor temp
    anchor = list(sorted_temperature_dict.values())[0]

    # initialize length
    length = 0

    # increase length and reset anchor if index <= current anchor or == +1
    for k,v in sorted_temperature_dict.items():
        if v <= anchor or v == anchor + 1:
            length += 1
            anchor = v
        else:
            break
    return length

if __name__ == '__main__':
    T = [5, -2, 3, 8, 6]
    print(solution(T))
    T = [-5, -5, -5, -42, 6, 12]
    print(solution(T))

