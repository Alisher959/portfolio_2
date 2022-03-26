def al(n):
    r=0
    for i in range(2,n+1,2):
        r+=i
    return r 
n=int(input('sonni kiriting '))
print(al(n))
