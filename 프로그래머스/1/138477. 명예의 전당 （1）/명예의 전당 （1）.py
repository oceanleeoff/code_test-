def solution(k, score):
    answer = []
    honor_score = []
    
    for i in score : 
        if len(honor_score) < k :
            honor_score.append(i)
            honor_score.sort()
            
        else :
            if honor_score[0] < i :
                honor_score[0] = i
                honor_score.sort()
        
        answer.append(honor_score[0])
        
    return answer