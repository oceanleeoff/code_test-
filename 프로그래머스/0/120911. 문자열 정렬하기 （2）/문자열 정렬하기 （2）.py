def solution(my_string):
    str1 = my_string.lower()
    str1 = list(str1)
    str1.sort()
    return ''.join(str1)
