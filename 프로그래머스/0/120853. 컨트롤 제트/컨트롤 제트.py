def solution(s):
    result = []
    s_list = s.split()
    
    for i in s_list :
        if i == 'Z' :
            result.pop()
        else :
            result.append(int(i))
    
    return sum(result)