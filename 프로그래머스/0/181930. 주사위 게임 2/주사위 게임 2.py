def solution(a, b, c):
    total = a + b + c
    square_sum = a**2 + b**2 + c**2 
    cube_sum = a**3 + b**3 + c**3
    
    if a == b == c :
        return total * square_sum * cube_sum
    elif (a == b) or (b == c) or (a == c) :
        return total * square_sum
    else :
        return total
    