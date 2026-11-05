#5.	 Crie um programa que simule uma calculadora simples. 
# O usuário deve informar a operação desejada e os dois números para realizar o cálculo. 
# As operações podem ser: adição, subtração, multiplicação e divisão.

operacao = str(input("digite a operação que você quer fazer: "))
num1 = int(input("Escreva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))

if operacao == "adição":
    soma = num1 + num2
    print ("O número " , num1 , " Somado com o número " , num2 , " é igual a " , soma)

elif operacao == "subtração":
    menos = num1 - num2
    print ("O número " , num1 , " Diminuido pelo número " , num2 , " é igual a " , menos)

elif operacao == "multiplicação":
    vezes = num1 * num2
    print ("O número " , num1 , " Multiplicado pelo número " , num2 , " é igual a " , vezes)

else:
    dividir = num1 / num2
    print ("O número " , num1 , " Dividido pelo número " , num2 , " é igual a " , dividir)