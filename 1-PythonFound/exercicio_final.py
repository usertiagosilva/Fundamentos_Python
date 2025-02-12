teams = {}
done = False

# Função para listar times
def print_teams():
    if not teams:
        print("Nenhum time cadastrado.")
        return
    print("\nTimes listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

# Função para listar jogadores de um time
def print_team_players(team):
    if not team['players']:
        print(f"O time {team['name']} ainda não tem jogadores cadastrados.")
        return
    print(f"\nJogadores do {team['name']}:")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")

# Loop do menu principal
while not done:
    print("\n=== Gerenciamento de Times ===")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input("Escolha uma opção: ")
    
    # Adicionar um time
    if choice == "1":
        team_name = input("Digite o nome do time: ").strip()
        if team_name in teams:
            print("Este time já está cadastrado!")
        else:
            teams[team_name] = {'name': team_name, 'players': []}
            print(f"Time '{team_name}' adicionado!")  
    
    # Remover um time
    elif choice == "2":
        print_teams()
        try:
            team_num = int(input("Informe o número do time para remover: "))
            team_list = list(teams.keys())
            if 1 <= team_num <= len(team_list):
                team_name = team_list[team_num - 1]
                del teams[team_name]
                print(f"Time '{team_name}' removido.")
            else:
                print("Número de time inválido.")
        except ValueError:
            print("Digite um número válido!")
    
    # Listar times
    elif choice == "3":
        print_teams()
    
    # Adicionar jogador em um time
    elif choice == "4":
        print_teams()
        try:
            team_num = int(input("Informe o número do time: "))
            team_list = list(teams.keys())
            if 1 <= team_num <= len(team_list):
                team_name = team_list[team_num - 1]
                player_name = input("Informe o nome do jogador: ").strip()
                teams[team_name]['players'].append(player_name)
                print(f"Jogador '{player_name}' adicionado ao time '{team_name}'!")
            else:
                print("Número do time inválido.")
        except ValueError:
            print("Digite um número válido!")
    
    # Remover jogador de um time
    elif choice == "5":
        print_teams()
        try:
            team_num = int(input("Informe o número do time: "))
            team_list = list(teams.keys())
            if 1 <= team_num <= len(team_list):
                team_name = team_list[team_num - 1]
                print_team_players(teams[team_name])
                try:
                    player_num = int(input("Informe o número do jogador para remover: "))
                    if 1 <= player_num <= len(teams[team_name]['players']):
                        removed_player = teams[team_name]['players'].pop(player_num - 1)
                        print(f"Jogador '{removed_player}' removido do time '{team_name}'.")
                    else:
                        print("Número do jogador inválido!")
                except ValueError:
                    print("Digite um número válido!")
            else:
                print("Número do time inválido.")
        except ValueError:
            print("Digite um número válido!")

    # Listar jogadores de um time
    elif choice == "6":
        print_teams()
        try:
            team_num = int(input("Informe o número do time: "))
            team_list = list(teams.keys())
            if 1 <= team_num <= len(team_list):
                print_team_players(teams[team_list[team_num - 1]])
            else:
                print("Número do time inválido.")
        except ValueError:
            print("Digite um número válido!")

    # Sair
    elif choice == "7":
        print("Saindo do programa...")
        done = True
    else:
        print("Opção inválida, tente novamente.")
