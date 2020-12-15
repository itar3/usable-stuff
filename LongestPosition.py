def longestpositionDP(alist):
    memo = [0] * len(alist)
    if alist[0] > 0:
        memo[0] = 1
    else:
        memo[0] = 0

    maxi = memo[0]
    for i in range(1, len(alist)):
        if alist[i] > 0:
            memo[i] = memo[i - 1] + 1
        else:
            memo[i] = 0
        if maxi < memo[i]:
            maxi = memo[i]
    return maxi


alist = [1, 2, 0, 5, 1, 7, 8, 9, 0, 1, 0, 0, -5, -9, -7, 1]
print(longestpositionDP(alist))


def maxSubsequenceDP(alist):
    memo = [0] * len(alist)
    memo[0] = alist[0]

    maxi = memo[0]
    for i in range(1, len(alist)):
        memo[i] = max(alist[i], alist[i] + memo[i - 1])
        if maxi < memo[i]:
            maxi = memo[i]
    return maxi


blist = [1, 2, 0, -4, 1, 2, 96, -1, -100, 99, 0, 0, -5, -9, -7, 25]
clist = [90, 90, 0, -200, 1, 2, 96, -1, -100, 99, 0, 0, -5, -9, -7, 25]
print(maxSubsequenceDP(blist))
print(maxSubsequenceDP(clist))


