def ricercaLineare(v,x):
    for i in range(len(v)):
        if v[i]==x:
            return True
    return False

A=[1,2,4,2,6,7,8,5,4,3]
print(ricercaLineare(A,3))
print(ricercaLineare(A,9))
