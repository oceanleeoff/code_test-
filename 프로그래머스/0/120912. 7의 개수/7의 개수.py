def solution(array):
    answer = 0
    
    for i in array :
        str_i = str(i)
        answer += str_i.count('7')
        
    return answer