def solution(polynomial):
    polynomial_list = polynomial.split(' ')
    coef_x = 0
    constant = 0
    
    for i in polynomial_list :
        if i == '+' :
            continue
        elif i == 'x' :
            coef_x += 1
        elif 'x' in i :
            coef_x += int(i[:-1])
        else :
            constant += int(i)
        
    if coef_x and constant :
        if coef_x == 1 :
            return f'x + {constant}'
        else :
            return f'{coef_x}x + {constant}'
    elif coef_x:
        return 'x' if coef_x == 1 else f'{coef_x}x'
    else :
        return str(constant)
        