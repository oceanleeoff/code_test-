def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    
    for i in str_num :
        if str_k == i :
            return str_num.index(i) + 1
        elif str_k not in str_num :
            return -1