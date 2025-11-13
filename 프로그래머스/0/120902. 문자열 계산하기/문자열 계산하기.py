def solution(my_string):
    num_list = []
    str_list = my_string.split(' ')
    temp = ''
    operation = '+'
    
    for i in str_list :
        if (i == '+') or (i == '-') :
            operation = i
        elif i.isdigit():
            if operation == '+':
                num_list.append(int(i))
            else :
                num_list.append(-int(i))

    return sum(num_list)