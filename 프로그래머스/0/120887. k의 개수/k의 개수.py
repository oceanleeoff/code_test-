def solution(i, j, k):
    answer = 0
    str_k = str(k)
    
    for n in range(i, j+1) :
        answer += str(n).count(str_k)

    return answer