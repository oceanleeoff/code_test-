def solution(dots):
    x_values = [x for x, y in dots]
    y_values = [y for x, y in dots]

    h = max(x_values) - min(x_values)
    v = max(y_values) - min(y_values)
    
    return h * v