def solution(array):
    num_list = set(array)
    freq = []
    
    # 빈도 수 추가
    for i in num_list :
        freq.append(array.count(i))
    
    # 최대 빈도 수
    max_freq = max(freq)
    
    # 최대 빈도 수의 동일 값이 여러 개인 경우
    if freq.count(max_freq) > 1:
        return -1
    
    # 최대 빈도 수의 인덱스 번호
    max_freq_index = freq.index(max_freq)
    
    return list(num_list)[max_freq_index]