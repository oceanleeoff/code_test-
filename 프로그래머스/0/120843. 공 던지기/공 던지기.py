def solution(numbers, k):
    i = (2 * (k - 1)) % len(numbers)
    return numbers[i]