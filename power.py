__author__ = 'keleigong'
def power(x,n):
    if n == 0:
        return 1
    if abs(n) == 1:
        result = x
    else:
        half = power(x,abs(n)/2)
        if abs(n) % 2 == 0:
            result = half * half
        else:
            result = half * half * x
    if n > 0:
        return result
    else:
        return 1.0/result

def cents(n,i):
    if i == 4:
        return [n]
    base = [50,25,10,5,1]
    if n >= base[i]:
        return [n/base[i]]+cents(n%base[i],i+1)
    else:
        return [0] + cents(n,i+1)

def cents2(n):
    base = [50, 25, 10, 5, 1]
    result = []
    for i in base:
        if n >= i:
            result.append(n/i)
            n = n % i
        else:
            result.append(0)
    return result

def cents3(n):
    # if n == 0:
    #     return []
    base = [50, 25, 10, 5, 1]
    for i in base:
        if n >= i:
            return [i] + cents3(n-i)

    return []