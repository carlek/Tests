def cumsum(V):
    result = [V[0]]
    for i in range(1, len(V)):
        sum = result[i-1] + V[i]
        result.append(sum)
    return result

def solution(A):
    a_rev = list(reversed(A))                           
    a_sum = cumsum(A)                               
    a_sum_rev = cumsum(a_rev)       
                                                        
    answer = []                                         
    for n, (i, j) in enumerate(zip(a_sum, a_sum_rev)):  
        if i == j:                                      
            answer.append(n)                            
    if answer:                                          
        return answer                                   
    else:                                               
        return -1                                       
    pass

import random
A = [-1, 3, -4, 5, 1, -6, 2, 1]
A = [random.randint(0,3) for i in range(1000)]
print(solution(A))