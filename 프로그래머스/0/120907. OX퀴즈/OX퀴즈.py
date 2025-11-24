def solution(quiz):
    answer = []
    
    for i in quiz :
        x, op, y, eq, z = i.split()
        x, y, z = int(x), int(y), int(z)
        
        if op == '+' :
            result = x + y
        else :
            result = x - y
        
        if result == z :
            answer.append('O')
        else :
            answer.append('X')
    
    return answer