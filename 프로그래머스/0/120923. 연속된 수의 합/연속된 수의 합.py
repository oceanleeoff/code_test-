def solution(num, total):
    start_num = (total // num) - ((num - 1) // 2)
    
    return [start_num + i for i in range(num)]

