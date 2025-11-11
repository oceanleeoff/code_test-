def solution(numer1, denom1, numer2, denom2):
    denom3 = denom1 * denom2
    numer3 = (numer1 * denom2) + (numer2 * denom1)
    
    for i in range(min(numer3, denom3), 0, -1) :
        if (denom3 % i == 0) and (numer3 % i == 0) :
            return [numer3 // i, denom3 // i]
