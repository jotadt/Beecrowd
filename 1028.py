def mdc(x,y):
    resto = None
    while resto != 0:
        resto = x % y
        x = y
        y = resto
    return x
    
trocas = int(input())
for i in range(trocas):
    numeros = [int(num) for num in input().strip().split(' ')]
    print(mdc(numeros[0], numeros[1]))