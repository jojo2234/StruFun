def binario(n):
    if n==0:
        return ''
    return binario(n//2)+str(n%2)
print(binario(72))
