def solution(n, arr1, arr2):
    answer = []
    
    temp1 = [bin(i)[2:].zfill(n) for i in arr1]
    temp2 = [bin(j)[2:].zfill(n) for j in arr2]
            
    for a, b in zip(temp1, temp2) :
        temp3 = ''
        
        for c, d in zip(a, b) :
            if (c == '1') or (d == '1') :
                temp3 += '#'
            else : 
                temp3 += ' '
                
        answer.append(temp3)
        
    return answer