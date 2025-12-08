def solution(a, b, n):
    answer = 0
    empties = n
    
    while empties >= a :
        new_coke = empties // a
        answer += b*new_coke
        empties = empties - (new_coke * a) + (new_coke * b) 

    return answer