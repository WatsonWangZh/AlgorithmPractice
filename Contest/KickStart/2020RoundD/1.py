
T = int(input())
for t in range(T):
    N = input()
    res = 0
    
    a = list(map(int, input().split()))
    if N == 1 or len(a) <= 1:
        res += 1
        print('Case #%d: %d' % (t+1, res))
        continue
    
    pre_max = float('-inf')
    for i in range(1, len(a)-1):
        pre_max = max(pre_max, a[i-1])
        if pre_max < a[i] and a[i] > a[i+1]:
            res += 1
    
    if a[-1] > max(a[:len(a)-1]):
        res += 1

    if a[0] > a[1]:
        res += 1
    print('Case #%d: %d' % (t+1, res))