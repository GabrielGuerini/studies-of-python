print('='*30, '🔮Bem vindo ao Oráculo da Programação👨🏻‍💻', '='*30)

tema = input("Digite o tema de programação que você quer saber: ")

match tema:
    case "python":
        print("Python é incrível, e de facil aprendizagem..")
    case "html":
        print("HTML cria páginas web!")
    case "css":
        print("CSS estiliza páginas!")
    case _:
        print("Ainda estou aprendendo esse tema.")
