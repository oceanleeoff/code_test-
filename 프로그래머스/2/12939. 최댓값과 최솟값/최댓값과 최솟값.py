def solution(s):
    temp = []
    
    for i in s.split(' ') :
            temp.append(int(i))
    
    max_s = str(max(temp))
    min_s = str(min(temp))
    
    return min_s + ' ' + max_s