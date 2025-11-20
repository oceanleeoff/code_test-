def solution(score):
    mean_list = []
    for i in score :
        mean_list.append((i[0]+i[1]) / 2)
    
    mean_sorted = sorted(mean_list, reverse=True)
    
    return [mean_sorted.index(i) + 1 for i in mean_list]