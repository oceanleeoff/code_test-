def solution(s):
    answer = []
    start_word = True
    
    for i in s :
        if i == ' ' :          # 공백일 경우 시작으로  초기호
            answer.append(i)
            start_word = True
            
        else :                 # 첫 글자
            if start_word :
                
                if i.isdigit() :
                    answer.append(i)
                else :
                    answer.append(i.upper())    
    
                start_word = False
            
            else :              # 중간 글자
                answer.append(i.lower())
                
    return ''.join(answer)