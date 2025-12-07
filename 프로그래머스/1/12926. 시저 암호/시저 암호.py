def solution(s, n):
    result = []
    for i in s:
        if i == ' ':
            result.append(' ')
        elif i.isupper(): 
            result.append(chr((ord(i) - ord('A') + n) % 26 + ord('A')))
        else:  
            result.append(chr((ord(i) - ord('a') + n) % 26 + ord('a')))
    return ''.join(result)