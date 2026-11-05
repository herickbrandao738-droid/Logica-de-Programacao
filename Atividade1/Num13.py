#13.	Verificar se um número é par ou ímpar
#Peça para o usuário inserir um número e mostre se ele é "Par" ou "Ímpar".

num = int(input("Digite um número: "))
if num % 2 == 0:
    print ("O número é par")
else:
    print ("O número é ímpar")