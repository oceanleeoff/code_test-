def solution(s):
    cnt_transform = 0
    del_zero_cnt = 0
    
    while s != '1' :
        zero_cnt = s.count('0')   # 제거할 0의 개수 카운트
        del_zero_cnt += zero_cnt
        
        s = s.replace('0', '')
        len_s = len(s)
        
        s = bin(len_s)[2:]
        
        cnt_transform += 1
        
    return [cnt_transform, del_zero_cnt]