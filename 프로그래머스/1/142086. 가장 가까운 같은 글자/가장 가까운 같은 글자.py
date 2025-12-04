def solution(s):
    answer = []
    last_seen = {}
    
    for i, w in enumerate(s):
        if w in last_seen:
            answer.append(i - last_seen[w]) 
        else:
            answer.append(-1)
        last_seen[w] = i  
    
    return answer