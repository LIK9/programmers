def solution(n):
    answer = 0
    
    answer = n**(1/2)
    
    if (int(answer) != answer):
        answer = -1
    else:
        answer += 1
        answer = answer**2
    
    return answer

