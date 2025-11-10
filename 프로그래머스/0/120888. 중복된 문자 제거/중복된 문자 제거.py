def solution(my_string):
    str_list = []
    str1 = list(my_string)
    for i in str1 :
        if i not in str_list :
            str_list.append(i)
            
    return ''.join(str_list)