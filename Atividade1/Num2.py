peso = int(input("Escreva o seu peso: "))
planeta = int(input("Escreva o número do seu planeta: "))
if planeta == 1:
    pesoMercurio = peso/10 * 0.37
    print ("Seu peso em Mercúrio é: " , pesoMercurio)

elif planeta == 2:
    pesoVenus = peso/10 * 0.88
    print ("Seu peso em Vênus é: " , pesoVenus)

elif planeta == 3:
    pesoMarte = peso/10 * 0.38
    print ("Seu peso em Marte é: " , pesoMarte)

elif planeta == 4:
    pesoJupiter = peso/10 * 2.64
    print ("Seu peso em júpiter é: " , pesojupiter)

elif planeta == 5:
    pesoSaturno = peso/10 * 1.15
    print ("Seu peso em Saturno é: " , pesoSaturno)
    
else:
    pesoUrano = peso/10 * 1.17
    print ("Seu peso em Urano é: " , pesoUrano) 