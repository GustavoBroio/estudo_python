print("****************************************")
print("Olá, bem-vindo ao jogo de adivinhação!!")
print("****************************************")

numero_secreto = 42

chute_srt = input("Digite o um número: ")

print("Você digitou: ", chute_srt)

chute = int(chute_srt)

acertou = numero_secreto == chute

if (acertou):
    print(" Você acertou! ")
else:
    if(chute>numero_secreto):
        print("Você errou! o chute foi maior que o número secreto...")
    if(chute<numero_secreto):
        print("Você errou! o chute foi menor que o número secreto...")

print("Fim do jogo!!")