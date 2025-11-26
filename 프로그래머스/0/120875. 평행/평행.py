def solution(dots):
    def incline(a, b) :
        return ((b[1] - a[1]) / (b[0] - a[0]))
    
    if incline(dots[0], dots[1]) == incline(dots[2], dots[3]) :
        return 1
    elif incline(dots[0], dots[2]) == incline(dots[1], dots[3]) :
        return 1
    elif incline(dots[0], dots[3]) == incline(dots[1], dots[2]) :
        return 1
    else : 
        return 0