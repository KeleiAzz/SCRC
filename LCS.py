__author__ = 'keleigong'
'''Longest Common Subsequence'''


def LCS(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if len(x) > 1 and len(y) > 1:
        if x[-1] == y[-1] and x[-2] == y[-2]:
            return LCS(x[:-1], y[:-1]) + x[-1]
        elif x[-1] == y[-1] and x[-2] != y[-2]:
            return LCS(x[:-1], y[:-1]) + '*' + x[-1]
        else:
            case2 = LCS(x[:-1], y)
            case3 = LCS(x, y[:-1])
            return case2 if len(case2) > len(case3) else case3
    else:
        if x in y:
            return x
        elif y in x:
            return y

print LCS('DACDCABCABDA', 'DACDCABDACDABCCBD')
print LCS('DACDCABDACDABCCBD', 'DACDCABCABDA')

def LCSeq(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return LCSeq(x[:-1], y[:-1]) + x[-1]
    else:
        case2 = LCSeq(x[:-1], y)
        case3 = LCSeq(x, y[:-1])
        # if len(case2) == len(case3):
        #     return case2 + '*' + case3
        return case2 if len(case2) > len(case3) else case3


print LCSeq('DACDCABCABDA', 'DACDCABDACDABCCBD')