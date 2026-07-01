print("=== Sistema de Notas da Escola ===")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Parabéns! Você foi aprovado com média {media:.2f}.")

elif media >= 5:
    print(f"Você ficou em recuperação com média {media:.2f}.")

    precisa = 14 - media

    print(f"Para ser aprovado, você precisa tirar pelo menos {precisa:.2f} na recuperação.")

    recuperacao = float(input("Digite a nota da recuperação: "))

    media_final = (media + recuperacao) / 2

    if media_final >= 7:
        print(f"Parabéns! Você foi aprovado na recuperação com média final {media_final:.2f}.")
    else:
        print(f"Você foi reprovado. Sua média final foi {media_final:.2f}.")

else:
    print(f"Você foi reprovado direto com média {media:.2f}.")