#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('Você é do sexo feminino ou masculino? Digite com M ou F:')
genero = input()
generos = ['m', 'f']


if genero == 'm':
    print('masculino')
elif genero == 'f':
    print ('feminino')
else:
    print ('invalido')