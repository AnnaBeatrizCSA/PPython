import random

print("Adivinhe o Número Secreto!")
print("Eu pensei em um número entre 1 e 50... você tem 10 tentativas!\n")

numero_secreto = random.randint(1, 50)
tentativas = 0
limite_tentativas = 10
acertou = False

while tentativas < limite_tentativas and not acertou:
    palpite = int(input(f"Tentativa {tentativas + 1}/{limite_tentativas} - Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto}, em {tentativas} tentativas.")
        acertou = True
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR que isso.")
    else:
        print("O número secreto é MENOR que isso.")

if not acertou:
    print(f"Suas tentativas acabaram! O número era {numero_secreto}. Tente novamente!")
