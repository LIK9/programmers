def solution(s):
    answer = False
    cnt = 0
    for word in s:
        if word == '(':
            cnt += 1
        elif word == ')':
            if cnt == 0:
                return False
            cnt -= 1


    return cnt == 0