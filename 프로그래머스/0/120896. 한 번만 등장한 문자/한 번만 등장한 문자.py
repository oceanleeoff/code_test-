def solution(s):
    answer = []
    
    for i in s :
        cnt = 0
        
        for j in s :
            if j == i :
                cnt += 1
                
        if cnt == 1 :
            answer.append(i)
            
    answer.sort()
    
    return ''.join(answer)