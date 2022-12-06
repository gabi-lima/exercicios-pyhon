#Exercício 1.2
#Inicialize o interpretador do Python e use-o como uma calculadora.

#Quantos segundos há em 42 minutos e 42 segundos?

#Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
#Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

minutos = 42

segundos = 42

totalsegundos = (minutos * 60) + 42

print ('Resposta 1 questão: a quantidade de segundos é', totalsegundos)

quilometros = 10

milhas = quilometros / 1.61

resultado = round(milhas, 2)
#resultado = f'{milhas:.2f}' - outra forma de limitar os caractéres, transformando em float.

print ('Reposta 2 questão:', quilometros, 'quilômetros em milhas são', resultado, "milhas")
#print (resultado)

#milhas por minuto
milhasminutos = milhas / (totalsegundos / 60)
resultadoMiMi = round(milhasminutos, 2)

#milhas por hora
milhashora = milhas / milhasminutos / 60
resultadoMiHo = round(milhashora, 2)
print ('Repostas 3 questão: Seu passo médio é de:', resultadoMiMi, " milhas por minuto, e ", resultadoMiHo, 'milhas por hora.')

