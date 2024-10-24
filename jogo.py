esquerda = 1
frente = 1 

print("\nBem-vindo à Aventura na Floresta Encantada")
print("\nUma vez a floresta encantada era bela após uma sudita invasão dos montros virou um caos completo milhares de pessoas morreram, a floresta que um dia foi bela hoje está banhada por sangue humano.")
print("\nUm sacerdote teve uma visão, um humano que combatia os montros e traria a paz e a beleza da floresta encantada de volta, então após longos 50 anos o heroi nasceu e com isso a história que vais jogar.")
print("\nApós o heroi crescer foi para a floresta encantada e agora a aventura começa sendo tu o personagem principal.")

print("\nPerto da floresta o heroi pergunta se realmente quer seguir em frente.")

direcao = input("Seguir em frente/sair: ")
if direcao == "frente":
    print("Entrando na floresta.")
    nome = input("Insira o seu nick: ")

    print(f"\nEntrando pela floresta a dentro {nome} vê dois caminhos um pela direita outro pela esquerda qual deles escolhes?")

    escolha = input("(direita/esquerda):")

    if escolha == "esquerda":
        print("\nTu morreste!")
    else:
        print("\nEntraste num local com cheiro intenso a sangue.")
        
else:
    print("\nIndo embora da floresta, quando estiveres preparado podemos retornar.")
