print("\nBem-vindo à Aventura na Floresta Encantada")
print("\nUma vez a floresta encantada era bela após uma sudita invasão dos montros virou um caos completo milhares de pessoas morreram, a floresta que um dia foi bela hoje está banhada por sangue humano.")
print("\nUm sacerdote teve uma visão, um humano que combatia os montros e traria a paz e a beleza da floresta encantada de volta, então após longos 50 anos o heroi nasceu e com isso a história que vais jogar.")
print("\nApós o heroi crescer foi para a floresta encantada e agora a aventura começa sendo tu o personagem principal.")

print("\nPerto da floresta o heroi pergunta se realmente quer seguir em frente.")

direcao1 = input("Seguir/sair: ")#variável para fazer uma escolha
direcao2 = direcao1.lower()#editor para fazer com que a variavel funcione com e sem ser maisculo
if direcao2 == "seguir":#função da variavel
    print("Entrando na floresta.")
    nome = input("Insira o seu nick: ")#variavel de inserção de nome

    print(f"\nEntrando pela floresta a dentro {nome} vê dois caminhos um pela direita outro pela esquerda qual deles escolhes?")

    escolha = input("(direita/esquerda): ")#variavel de escolha

    if escolha == "esquerda":#se escolha for esquerda o jogador perde o jogo
        print("\nEncontraste monstros")
        print("\nGAME OVER!")
    else:#se não o jogador avança para o proximo estagio
        print("\nEntraste num local com cheiro intenso a sangue.")

        print(f"\nOlhando para o chão, {nome} verifica que existem corpos de antigos guerreiros desmenbrados e torturados até a morte.")
        print(f"\n{nome} verifica que tem uma espada no chão deseja apanhá-la?: ")
        escolha2 = input("(Pegar/Não pegar): ")
        if escolha2 == "Pegar" or escolha2 == "pegar":#se escolha de pegar um item no chão
            print("Espada adicionada ao inventário.")
            inventario = ["espada"]
        else:#se não, ignorar o item no chão
            print("(Espada foi ignorada)")
        print("Seguindo em frente encontras orcs desejas atacá-los de surpresa ou stealh mode: ")
        escolha3 = input('AtaqueSurpresa(A) / SteatlhMode (S): ')
        if escolha3 == "A":#se escolheres A de Ataque morres 
                                                                    #escolhas de avanço de fase / decisão antes de chegar no fim do jogo
            print("Tomaste HitKill por não teres armadura.")
        else:#se não avanças e ganhas o jogos destruindo o núcleo
            print("Chegas-te no Núcleo e destruiste-o matando todos os monstros.")
            print("YOU WIN!")
else:#Fim de jogo causado pela negação de avançar
    print("\nIndo embora da floresta, quando estiveres preparado podemos retornar.")

#As funções if/elif/else estão a ser utilizadas para obrigar o usuario a fazer escolhas entre um ,outro ou outro.
#As funçoes input depois da variavel é para obrigar o usuario a fazer um escolha e depois faz com que a escolha do usuario ganhe valor
#As funções print estão a ser utilizadas para demonstrar a historia e informar.
