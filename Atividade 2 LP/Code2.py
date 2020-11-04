import math

p=float
area=float

a= int(input('Digite o valor de A:'))
b= int(input('Digite o valor de B:'))
c= int(input('Digite o valor de C:'))

p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c))

if(a > b + c):
    print('Não forma um Triângulo!')
    print('O valor de A é: ',a,'\nO valor de B é:',b,'\nO Valor de c é:',c)

if(area > 0):
    print('É um Triângulo!')
    print('A Área do Triângulo é %0.2f'%math.sqrt(area))

