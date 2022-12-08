#Faça um Programa que peça dois números e imprima o maior deles.
#1 exercicio

print('Vamos descobrir qual número é maior!')
print('Digite o primeiro número:')
primeiroNumero = input()
print('Digite o segundo número:')
segundoNumero = input()
#print(primeiroNumero, segundoNumero)

if primeiroNumero == segundoNumero:
    print(primeiroNumero, 'é igual a', segundoNumero)
else:
    if primeiroNumero > segundoNumero:
        print(primeiroNumero, 'é maior que', segundoNumero)
    else:
        print(segundoNumero, 'é maior que', primeiroNumero)
