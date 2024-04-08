def solution(s):
    answer = ''
    
    arr = list(map(int, s.split()))
    
    max_val = max(arr)
    min_val = min(arr)
    answer = str(min_val) + ' ' + str(max_val)
    
    
    return answer