def solution(emergency):
    em_sorted = sorted(emergency, reverse=True)
    return [em_sorted.index(i) + 1 for i in emergency]