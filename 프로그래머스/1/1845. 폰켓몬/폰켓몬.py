def solution(nums):
    n = len(nums)
    comb_n = len(set(nums))  # 선택 가능한 수 
    
    select = n // 2
    
    return min(comb_n, select)