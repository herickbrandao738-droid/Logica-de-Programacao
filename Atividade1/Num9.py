#9.	Crie um programa que calcule o desconto a ser aplicado em uma compra. 
# O usuário deve informar o valor total da compra e o tipo de cliente (Regular, VIP ou Funcionário). 
# As regras para o desconto são:
#●	Regular: 0% de desconto
#●	VIP: 10% de desconto
#●	Funcionário: 20% de desconto

compra = float(input("Digite o valor total da compra: "))
cliente = str(input("Digite o tipo de cliente que você é: "))

if cliente == "Regular":
    print ("Você é um cliente regular, não tem desconto. O valor final da compra é: " , compra)
elif cliente == "VIP":
    compraVIP = compra - (compra*0.1)
    print ("Você é vip, e tem um desconto de 10%. O valor final da sua compra é: " , compraVIP)
else:
    compraFuncionario = compra - (compra*0.2)
    print ("Você é um funcionário, e tem um desconto de 20%. O valor final da sua compra é: " , compraFuncionario)