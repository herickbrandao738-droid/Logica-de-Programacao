#8.	Faça um programa que permita o cadastro de produtos em uma empresa. 
# O usuário deve informar o tipo de produto (Alimento, Bebida, Vestuário). 
# O programa deve exibir uma mensagem de confirmação com o tipo de produto cadastrado e se ele 
# é perecível ou não, de acordo com as seguintes regras:
#●	Alimento: Perecível
#●	Bebida: Não Perecível
#●	Vestuário: Não Perecível

tipoProduto = str(input("Escreva o tipo de produto: "))
if tipoProduto == "Alimento":
    print ("Perecível")
else: 
    print ("Não perecível")