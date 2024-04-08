def solution(n):
    
    answer = 0
    f0 = 0
    f1 = 1
    f2 = 0
    for i in range(n-1):
        f2 = (f1 + f0) % 1234567
        f0 = f1
        f1 = f2
    answer = f2
        
    
    return answer