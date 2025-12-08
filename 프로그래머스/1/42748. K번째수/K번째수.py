def solution(array, commands):
    answer = []
    
    for s in commands :
        i, j, k = s[0]-1, s[1], s[2]-1
        sorted_array = sorted(array[i:j])
        answer.append(sorted_array[k])
        
    return answer