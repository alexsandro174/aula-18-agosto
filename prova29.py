#prova adeildo
#autor:alexsandro
#https://github.com/alexsandro174/prova-alternativas.git

import time
for i in range (10,-1,-1)
    print (i)
    time.sleep(1)
print ("BOOM!")


for i in range (1,51):
    if i % 2 ==0:
        print (i)


soma = 0
for i in range(1,51):
    if i % 2 !=0 and i % 3 ==0:
        soma +=i
print("a soma dos numeros impares multiplos de 3 entre 1 e 50 é",soma)

numero = int(input("digite um numero para ver sua tabuada:"))


soma_pares = 0
for i in range (6):
    numero = int(input("digite um número inteiro"))
if numero % 2 ==0
soma_pares += numero
print("a soma dos números pares digitados é: (soma_pares)")


primeiro_termo = int(input(digite o primeiro termo da PA))
razao = int(input("digite a razão da PA:"))
for i in range (10)
termo = primeiro_termo + i *razao
print (termo, end="")


#Verificar se frase é palíndromo
frase = input("Digite uma frase: ").replace(" ", "").lower()
if frase == frase[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")


#Maioridade (7 pessoas)
from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for i in range(7):
    ano = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    idade = ano_atual - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Maiores de idade: {maiores}")
print(f"Menores de idade: {menores}")


#Maior e menor peso (5 pessoas)
pesos = []

for i in range(5):
    p = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    pesos.append(p)

print("Maior peso:", max(pesos))
print("Menor peso:", min(pesos))


#Contagem progressiva de 0 a 10 (2 segundos)
import time

for i in range(11):
    print(i)
    time.sleep(2)

print("Você concluiu a tarefa em 20 segundos, parabéns! 🎉")