x = int(input())
y = int(input())

if x > y:
    a = y
    b = x
if x <= y:
    a = x
    b = y
soma = 0

while a <= b:
    if a % 13 != 0:
        soma = a + soma
    a = 1 + a
print(soma)