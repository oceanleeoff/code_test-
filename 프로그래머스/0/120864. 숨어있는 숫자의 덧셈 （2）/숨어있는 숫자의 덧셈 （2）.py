def solution(my_string):
    num_list = []
    temp = ''
    
    for i in my_string :
        if i.isdigit():
            temp += i
        else :
            if temp :
                num_list.append(int((temp)))
                temp = ''
    
    if temp :                       # else로 넘어가지 않는 마지막 숫자 처리
        num_list.append(int(temp))
    
    return sum(num_list)
    