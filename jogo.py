import game.json

# Carregar os dados do jogo a partir de um arquivo JSON
def load_game():
    with open('game.json', 'r', encoding='utf-8') as file:
        return json.load(file)

data = load_game()
player = {
    'location': data['startLocationId'],
    'inventory': [],
    'life': data['life'],
    'attack': data['attack'],
    'defense': data['defense'],
    'turns': 0,
    'max_turns': data.get('max_turns_normal', 0),
    'powers': [],
    'army': False
}

def navigate():
    current_location = next(loc for loc in data['locations'] if loc['id'] == player['location'])
    print(f"\nVocê está em {current_location['name']}.")
    print(current_location['description'])
    
    if 'items' in current_location:
        for item in current_location['items']:
            print(f"Você encontrou {item}!")
            player['inventory'].append(item)
    
    if 'enemy' in current_location:
        enemy = current_location['enemy']
        combate(enemy)
        return
    
    if 'exits' in current_location:
        print("Saídas disponíveis:")
        for exit in current_location['exits']:
            if not exit.get('inactive', False):
                print(f"- {exit['direction']}")
        direction = input("Para onde deseja ir? ").lower()
        selected_exit = next((e for e in current_location['exits'] if e['direction'] == direction), None)
        if selected_exit and not selected_exit.get('inactive', False):
            player['location'] = selected_exit['targetLocationId']
        else:
            print("Não é possível ir nessa direção.")
    else:
        print("Sem saídas. Você precisa resolver um desafio aqui.")
    
    player['turns'] += 1
    if player['turns'] > player['max_turns'] > 0:
        print("Você ultrapassou o limite de turnos. Game Over!")
        return
    
    navigate()

def combate(enemy):
    print(f"Você enfrenta {enemy['name']}! {enemy['description']}")
    while player['life'] > 0 and enemy['life'] > 0:
        print("(1) Atacar (2) Defender-se")
        acao = input("Escolha sua ação: ")
        if acao == '1':
            if player['attack'] > enemy['defense']:
                enemy['life'] -= player['attack']
                print(f"Você causa dano! Vida do {enemy['name']}: {enemy['life']}")
            else:
                print("Seu ataque não teve efeito!")
        elif acao == '2':
            print("Você se defende!")
        
        if enemy['life'] > 0:
            if enemy['attack'] > player['defense']:
                player['life'] -= enemy['attack']
                print(f"{enemy['name']} ataca! Sua vida: {player['life']}")
        
    if player['life'] <= 0:
        print("Você foi derrotado... Game Over!")
    else:
        print(f"Você venceu {enemy['name']}!")
        if 'drop' in enemy:
            print(f"Você encontrou {enemy['drop']}!")
            player['inventory'].append(enemy['drop'])
        navigate()

def start_game():
    print(f"Bem-vindo à {data['title']}!")
    print(data['description'])
    print(f"Autor: {data['author']}")
    print("Impeça Ana Jansen de despertar a serpente e dominar a ilha!")
    navigate()

start_game()
