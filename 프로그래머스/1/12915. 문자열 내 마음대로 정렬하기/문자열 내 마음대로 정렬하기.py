import functools

def sort_word(word, n) :
    return (word[n], word)

def solution(strings, n):
    word_func = functools.partial(sort_word, n=n)
    
    return sorted(strings, key=word_func)