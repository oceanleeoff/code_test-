def solution(babbling):
    p_word = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    
    for word in babbling :
        temp = word
        
        for p in p_word :
            if p in temp :
                temp = temp.replace(p, ' ', 1)
        
        if len(temp.strip()) == 0 :
            cnt += 1
        
    return cnt