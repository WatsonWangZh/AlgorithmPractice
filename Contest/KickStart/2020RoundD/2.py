# WA 
T = int(input())
for t in range(T):
    N = int(input())
    a = list(map(int, input().split()))

    res_inc = [0 for _ in range(N)]
    res_dec = [0 for _ in range(N)]
    
    for i in range(len(a)):
        i_max_inc = 0
        length = 0
        tmp = i
        while tmp+1 < len(a):
            if a[tmp+1] > a[tmp]:
                length += 1
            if a[tmp+1] == a[tmp]:
                tmp += 1
                continue
            tmp += 1
            i_max_inc = max(i_max_inc, length)
        res_inc[i] = i_max_inc   

    for i in range(len(a)):
        i_max_dec = 0
        length = 0
        tmp = i
        while tmp+1 < len(a):
            if a[tmp+1] < a[tmp]:
                length += 1
            if a[tmp+1] == a[tmp]:
                tmp += 1
                continue
            else:
                i_max_dec = max(i_max_dec, length)
                res_dec[i] = i_max_dec
                break
            tmp += 1
            i_max_dec = max(i_max_dec, length)
        res_dec[i] = i_max_dec 
         
    res = 0 
    for ele in res_inc:
        if ele and ele%4==0:
            res += 1
    for ele in res_dec:
        if ele and ele%4==0:
            res += 1 
    print(res_inc, res_dec)       
    print('Case #%d: %d' % (t+1, res))