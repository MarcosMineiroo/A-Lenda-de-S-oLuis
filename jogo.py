# A Lenda de São Luís - Jogo de Texto em Python
# Inspirado no folclore maranhense e na lenda da Serpente de São Luís
# Objetivo: Impedir que Ana Jansen desperte a serpente e domine a ilha

import json

# Variáveis globais
player = {
    'location': 'Alcantara',
    'inventory': [],
    'life': 3,
    'turns': 0,
    'max_turns': 30,
    'powers': [],
    'army': False
}

def start_game():
    print("Bem-vindo à Lenda de São Luís!")
    print("Impeça Ana Jansen de despertar a serpente e dominar a ilha!")
    print("Você começa em Alcântara. Explore e colete informações para enfrentar os desafios.")
    alcantara()

def alcantara():
    print("\nVocê está em Alcântara. Para onde deseja ir?")
    print("1. Igreja de Alcântara (Norte) - Falar com Sr. João sobre Ana Jansen")
    print("2. Taberna (Sul) - Resolver charada para conseguir a Espada de São Jorge")
    print("3. Igreja Velha (Leste) - Falar com Padre Loreno para saber o caminho do desafio")
    choice = input("Escolha uma opção: ")
    if choice == '1':
        historia_ana_jansen()
    elif choice == '2':
        charada_espada()
    elif choice == '3':
        padre_loreno()
    else:
        print("Escolha inválida.")
        alcantara()

def historia_ana_jansen():
    print("\nSr. João conta a história de Ana Jansen, a mulher poderosa que deseja controlar a serpente de São Luís...")
    print("Você descobre que ela quer despertar a serpente para dominar a ilha.")
    player['turns'] += 1
    alcantara()

def charada_espada():
    print("\nZezinho Pé de Cana te desafia com uma charada: 'Qual é a arma que corta sem machucar?' ")
    resposta = input("Qual é sua resposta? ")
    if resposta.lower() == 'palavra':
        print("\nVocê acertou! Zezinho te entrega a Espada de São Jorge.")
        player['inventory'].append('Espada de São Jorge')
    else:
        print("\nResposta errada. Tente novamente mais tarde.")
    player['turns'] += 1
    alcantara()

def padre_loreno():
    print("\nPadre Loreno revela que para chamar o Cabeça de Cuia, você deve gritar o nome 'Maria' três vezes.")
    player['turns'] += 1
    rio_itapecuru()

def rio_itapecuru():
    print("\nVocê chega ao Rio Itapecuru. O Cabeça de Cuia está à espreita.")
    if 'Espada de São Jorge' in player['inventory']:
        print("Você tem a Espada de São Jorge! Ela brilha com um poder misterioso.")
    else:
        print("Você não tem a espada certa para lutar. Talvez precise voltar a Alcântara.")
        alcantara()
    print("Você grita: Maria! Maria! Maria! O monstro emerge das águas...")
    batalha_cabeca_de_cuia()

def batalha_cabeca_de_cuia():
    print("\nA batalha contra o Cabeça de Cuia começa!")
    golpes = 0
    while golpes < 3 and player['life'] > 0:
        acao = input("Escolha sua ação: (1) Atacar a cabeça (2) Defender-se: ")
        if acao == '1':
            golpes += 1
            print(f"Você golpeia a cabeça do monstro! ({golpes}/3)")
        elif acao == '2':
            print("Você se defende, evitando um ataque brutal.")
        else:
            print("Ação inválida. Você perde uma chance.")
        player['turns'] += 1
    if golpes >= 3:
        print("Você derrotou o Cabeça de Cuia! As almas libertas mostram o caminho para o próximo desafio.")
        player['inventory'].append('Escudo Sagrado')
        raposa()
    else:
        player['life'] -= 1
        print("Você foi derrotado! Resta(m) " + str(player['life']) + " vida(s).")
        if player['life'] > 0:
            batalha_cabeca_de_cuia()
        else:
            print("Game Over! Ana Jansen desperta a serpente e domina São Luís.")
