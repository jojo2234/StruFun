def binomiale(n,k):
    if k==0 or k==n:
        return 1
    return binomiale(n-1,k-1) + binomiale(n-1,k)
print (binomiale(17,8))
