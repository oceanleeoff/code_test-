def solution(num_list, n):
    answer = [num_list[i*n : n*(i + 1)] for i in range(len(num_list) // n)]
    return answer