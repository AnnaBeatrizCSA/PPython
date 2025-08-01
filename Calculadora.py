import math
print ("----Escolha a operação que deseja----")
print (" 1-SOMA\n 2-SUBTRAÇÃO\n 3-MUTIPLICAÇÃO\n 4-DIVISÃO\n 5-POTENCIAÇÃO\n 6-RADIAÇÃO\n")
operacao = int(input("Digite a opção: "))
if operacao == 1:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    soma = a + b
    print("O resultado da soma é:" , soma)
elif operacao == 2:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    subtracao = a - b
    print("O resultado da subtração é:" , subtracao) 
elif operacao == 3:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    multiplicacao = a * b
    print("O resultado da multiplicação é:" , multiplicacao)     
elif operacao == 4:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    divisao = a / b
    print("O resultado da divisão é:" , divisao)    
elif operacao == 5:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    potenciacao = a ** b
    print("O resultado da potenciação é:" , potenciacao)            
elif operacao == 6:
    numero = int(input("Digite o número: "))
    raiz_quadrada = math.sqrt(numero)
    print("O resultado da radiação é:" , raiz_quadrada)
