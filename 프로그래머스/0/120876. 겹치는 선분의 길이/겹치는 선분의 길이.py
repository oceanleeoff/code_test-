def solution(lines):
    line = []
    
    for i in range(len(lines)) :
        for j in range(i+1, len(lines)) :
            a, b = lines[i]
            c, d = lines[j]
            start = max(a, c)
            end = min(b, d)
            if start < end :
                line.append([start, end])
    
    line.sort()
    new_line = []
    for s, e in line :
        if not new_line or new_line[-1][1] < s :
            new_line.append([s, e])
        else :
            new_line[-1][1] = max(new_line[-1][1], e)
            
    result = sum(e-s for s, e in new_line)
    
    return result