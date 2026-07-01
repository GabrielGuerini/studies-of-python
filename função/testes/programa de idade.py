print("Olá! Bem-vindo ao programa de cálculo de idade.")
idade = input("Digite sua idade: ")
print("Sua idade é:", idade)
idade_em_dias = int(idade) * 365
print("Sua idade em dias é:", idade_em_dias)
idade_em_horas = idade_em_dias * 24
print("Sua idade em horas é:", idade_em_horas)
idade_em_minutos = idade_em_horas * 60
print("Sua idade em minutos é:", idade_em_minutos)
idade_em_segundos = idade_em_minutos * 60
print("Sua idade em segundos é:", idade_em_segundos)
quantidade_de_dias_em_anos = 365
idade_em_anos = int(idade) / quantidade_de_dias_em_anos
print("Sua idade em anos é:", idade_em_anos)