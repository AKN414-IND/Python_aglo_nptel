def gcd(n,m):
    gcd_mn=0
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0 :
            gcd_mn=i
    return gcd_mn


print(gcd(12,18))




