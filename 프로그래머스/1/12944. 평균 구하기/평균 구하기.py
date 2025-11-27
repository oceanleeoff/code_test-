def solution(arr):
    answer = 0
    
    for i in arr :
        answer += int(i)
        
    return answer / len(arr)