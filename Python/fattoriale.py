def fattoriale(n):
    if n==0:
        return 1
    return n*fattoriale(n-1)

print(" 12! ", fattoriale(12))
print(" 18! ", fattoriale(18))
print(" 33! ", fattoriale(33))
