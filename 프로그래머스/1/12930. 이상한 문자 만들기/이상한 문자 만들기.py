def solution(s):
    answer = []
    s_list = s.split(' ')
    
    for i in s_list :
        temp = []
        for j in range(len(i)) :
            if j % 2 == 0 :
                temp.append(i[j].upper())
            else :
                temp.append(i[j].lower())
                
        answer.append(''.join(temp))
       
    return ' '.join(answer)