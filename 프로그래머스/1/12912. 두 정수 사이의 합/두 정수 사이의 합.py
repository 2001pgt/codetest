def solution(a, b):
    x = 0
    y = 0
    if a < b:
        x = a
        y = b
    elif a > b:
        x = b
        y = a
    else:
        return a
    
    answer = 0
    for i in range(x,y+1):
        
        answer += i
    return answer