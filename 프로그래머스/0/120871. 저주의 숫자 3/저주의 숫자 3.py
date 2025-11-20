def solution(n):
    num = 0
    cnt = 0
    
    while cnt < n :
        num += 1
        if ('3' in str(num)) or (num % 3 == 0) :
            continue
            
        cnt += 1
    
    return num