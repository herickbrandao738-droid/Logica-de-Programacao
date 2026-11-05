#16.	Comparação entre três números
#Peça para o usuário inserir três números e imprima o maior e o menor entre eles.
 
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maiorNum = num1
menorNum = num1

if num2 > maiorNum:
    maiorNum = num2

if num3 > maiorNum:
    maiorNum = num3

if num2 < menorNum:
    menorNum = num2

if num3 < menorNum:
    menorNum = num3

print ("O maior número é: " , maiorNum , "\nE o menor número é: " , menorNum)