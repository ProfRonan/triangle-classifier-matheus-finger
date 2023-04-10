a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b) and (b == c):
        print('Equilátero')
    elif (a == b) or (b == c) or (a == c):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não é um triângulo')