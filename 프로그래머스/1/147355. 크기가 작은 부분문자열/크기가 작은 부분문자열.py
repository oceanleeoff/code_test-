def solution(t, p):
    answer = 0
    len_p = len(p)
    num_p = int(p)
    
    for i in range(len(t) - len_p + 1) : 
        sub_num = int(t[i:i+len_p])
        if sub_num <= num_p :
            answer += 1
            
    return answer
