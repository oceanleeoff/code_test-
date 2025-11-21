def solution(numlist, n):
    def func(x):
        return (abs(x - n), -x)
    
    return sorted(numlist, key=func)

    
    