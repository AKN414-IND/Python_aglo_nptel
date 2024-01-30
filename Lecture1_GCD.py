def gcd(n,m):
    divisor_m=[]
    divisor_n=[]
    common_divisor=[]

    for i in range(1,min(n,m)+1):
        if n%i==0 :
            divisor_n.append(i)
        if m%i==0 :
            divisor_m.append(i)
    

    for i in divisor_n:
        if i in divisor_m:
            common_divisor.append(i)
    
    return max(common_divisor)


print(gcd(12,18))




            