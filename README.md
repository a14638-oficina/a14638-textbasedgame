<h1> TextBasedGame <h1>

<h1> Introdução ao Projeto 

Adicionar mais detalhes sobre a floresta e os monstros. Isso pode ajudar a criar uma atmosfera mais imersiva, o jogo foi criado com interesse em pessoas que leem e assistem animes e mangas e também para quem gosta de jogos de RPG. 

O jogo teve uma base em um manga que eu li e entre jogos que joguei, o jogo foi criado com base em múltiplos centros de interesse. 

Narrativa Interativa, escolhas do Jogador, sistema de Inventário mas ainda faltando utilização para o inventário, encontros e combate,  

Estrutura Narrativa 

O jogador é apresentado à história da floresta encantada, que foi destruída por monstros. Após o herói crescer, ele chega à entrada da floresta. O jogador deve decidir se deseja seguir em frente ou voltar. 

Lógica das Escolhas 

Escolha Inicial: Seguir ou Sair 

Caminhos Alternativos 

Direita ou esquerda 

Interações com o Ambiente 

O jogador deve decidir se quer pegar a espada, onde ele se depara entre a opção pegar ou a opção não pegar. 

Encontros com Inimigos 

O jogador depara-se com duas opções, o Ataque Surpresa, ou usar Stealth para passar sem ser percebido. 

Finais diferentes 

Com diferentes finais é possível ter muitas morte ou chegar ao final com maestria. 

Estrutura do Código  

O código não utiliza funções: 

Controle de Fluxo 

if direcao2 == "seguir": 

else: 

    print("\nIndo embora da floresta, quando estiveres preparado podemos retornar.") 

Esta condição verifica se o jogador deseja continuar a aventura ou não. Se a resposta for "seguir", o jogo prossegue. Caso contrário, termina. 

if escolha == "esquerda":  

print("\nEncontraste monstros")  

print("\nGAME OVER!")  

else: 

print("\nEntraste num local com cheiro intenso a sangue.") 

Aqui, a escolha entre "direita" ou "esquerda" determina se o jogador encontrará inimigos ou avança para um local seguro. 

Gestão de Dados 

Uso de Variáveis 

As variáveis são utilizadas para armazenar informações essenciais sobre o jogador e o estado do jogo. 

nome = input("Insira o seu nick: ") 

Armazena o nome do jogador, permitindo personalização e imersão na narrativa. 

direcao1 = input("Seguir/sair: ") 

Armazena a escolha do jogador, influenciando o fluxo da história. 

Uso de Listas 

inventario = ["espada"] 

Armazena os itens coletados pelo jogador. Com uma lista, você pode facilmente adicionar, remover ou verificar a presença de itens. 

Critérios de Uso 

Clareza e Simplicidade 

Flexibilidade 

Interatividade 

 

 

 

Interatividade com o Utilizador 

Uso da Função input(): Captura as decisões do jogador em momentos necessários. 

Decisão Inicial, 

Escolha de Caminho, 

Interação com Itens, 

Estratégia de Combate. 

Tratamento de Entradas 

Normalização: A entrada do jogador é convertida para minúsculas para evitar problemas com diferentes formatos de digitação. 

Desafio: Gerenciamento de Entradas do Usuário  

Um dos principais desafios ao recolher as entradas do jogador é garantir que as respostas sejam válidas e que o jogador não insira comandos inesperados ou errados para não dar erros inesperados. 

À medida que o jogo se torna mais complexo, o código pode ficar confuso e difícil de manter sem uma estrutura clara. 

Conclusão 

Eu pretendo melhorar o sistema de organização, fazer um esquema de inventário, e um esquema de combate o que vai demorar um bocado de acordo como eu sou por falta de criatividade em termos de escrita de código e a complexidade de fazer um sistema de lutas, e eu gostava de fazer o esquema de combate com base em jogos basicamente um esquema de batalha por turnos. </h1>
