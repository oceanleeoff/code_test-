def solution(array, n):
    num_sub = [abs(i - n) for i in array]
    min_diff = min(num_sub)
    
    num_list = [array[i] for i, diff in enumerate(num_sub) if diff == min_diff]
    return min(num_list)