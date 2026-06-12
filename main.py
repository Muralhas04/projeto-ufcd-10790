# main.py
import os
from dados import jogos
from logica import obter_tabela_ordenada, pesquisar_equipa

def limpar_ecran():
    """Limpa o terminal para o programa ficar mais limpo visualmente."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    limpar_ecran()
    print("=" * 40)
    print("           ★ TUGASCORE ★           ")
    print("   O Flashscore do Futebol Nacional   ")
    print("=" * 40)
    print(" 1. Liga Portugal (1ª Divisão)")
    print(" 2. Liga Portugal 2 (2ª Divisão)")
    print(" 3. Liga 3")
    print(" 4. Pesquisa de Equipas (Scouting)")
    print(" 0. Sair do Programa")
    print("=" * 40)

def mostrar_menu_divisao(nome_liga):
    while True:
        limpar_ecran()
        print("=" * 40)
        print(f" COMPETIÇÃO: {nome_liga.upper()} ")
        print("=" * 40)
        print(" 1. Ver Classificação Geral")
        print(" 2. Ver Resultados por Jornada")
        print(" 3. Ficha de Jogo Detalhada")
        print(" 0. Voltar ao Menu Principal")
        print("=" * 40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            exibir_classificacao(nome_liga)
        elif opcao == "2":
            exibir_jornadas(nome_liga)
        elif opcao == "3":
            exibir_ficha_jogo(nome_liga)
        elif opcao == "0":
            break
        else:
            print("\n❌ Opção Inválida! Pressione Enter para tentar novamente...")
            input()

def exibir_classificacao(nome_liga):
    limpar_ecran()
    tabela = obter_tabela_ordenada(nome_liga)
    print("=" * 65)
    print(f" CLASSIFICAÇÃO ATUAL - {nome_liga.upper()} ")
    print("=" * 65)
    print(f"{'Pos':<4}{'Equipa':<20}{'P':<5}{'J':<5}{'V':<5}{'E':<5}{'D':<5}{'GM':<5}{'GS':<5}")
    print("-" * 65)
    
    for i, (equipa, stats) in enumerate(tabela, 1):
        print(f"{i:<4}{equipa:<20}{stats['P']:<5}{stats['J']:<5}{stats['V']:<5}{stats['E']:<5}{stats['D']:<5}{stats['GM']:<5}{stats['GS']:<5}")
    
    print("=" * 65)
    input("\nPressione Enter para voltar...")

def exibir_jornadas(nome_liga):
    limpar_ecran()
    print(f"=== RESULTADOS POR JORNADA - {nome_liga} ===")
    
    if nome_liga not in jogos:
        print("\n⚠️ Nenhuns jogos registados nesta liga.")
        input("\nPressione Enter para voltar...")
        return
        
    try:
        jornada_escolhida = int(input("Introduza o número da Jornada (ex: 1): "))
        if jornada_escolhida in jogos[nome_liga]:
            print(f"\n--- JORNADA {jornada_escolhida} ---")
            for jogo in jogos[nome_liga][jornada_escolhida]:
                print(f" {jogo['casa']} {jogo['g_casa']} - {jogo['g_fora']} {jogo['fora']} ")
        else:
            print("\n❌ Jornada não encontrada!")
    except ValueError:
        print("\n❌ Erro: Por favor, introduza um número válido!")
        
    input("\nPressione Enter para voltar...")

def exibir_ficha_jogo(nome_liga):
    limpar_ecran()
    print(f"=== FICHA DE JOGO DETALHADA - {nome_liga} ===")
    
    if nome_liga not in jogos or 1 not in jogos[nome_liga]:
        print("\n⚠️ Sem dados disponíveis para esta liga.")
        input("\nPressione Enter para voltar...")
        return

    # Listar jogos disponíveis para o utilizador escolher
    lista_jogos = jogos[nome_liga][1] # Focado na jornada 1 para o protótipo
    print("\nEscolha um dos jogos para ver os detalhes:")
    for idx, jogo in enumerate(lista_jogos, 1):
        print(f" {idx}. {jogo['casa']} vs {jogo['fora']}")
        
    try:
        escolha = int(input("\nDigite o número do jogo: "))
        if 1 <= escolha <= len(lista_jogos):
            jogo = lista_jogos[escolha - 1]
            limpar_ecran()
            print("=" * 50)
            print(f" DETALHE DO JOGO: {jogo['casa']} {jogo['g_casa']} - {jogo['g_fora']} {jogo['fora']} ")
            print("=" * 50)
            
            print("\n⚽ GOLOS:")
            if not jogo['detalhes']['golos']:
                print("  (Sem golos gravados neste jogo)")
            for equipa, jogador, minuto in jogo['detalhes']['golos']:
                print(f"  • [{equipa}] {jogador} ({minuto}')")
                
            print("\n🟨 CARTÕES:")
            if not jogo['detalhes']['cartoes']:  
                print("  (Sem cartões gravados neste jogo)")
            for equipa, jogador, tipo, minuto in jogo['detalhes']['cartoes']:  
                print(f"  • [{equipa}] {jogador} - {tipo} ({minuto}')")
            print("=" * 50)
        else:
            print("\n❌ Jogo inválido!")
    except ValueError:
        print("\n❌ Erro: Entrada inválida!")
        
    input("\nPressione Enter para voltar...")

def exibir_pesquisa_scouting():
    limpar_ecran()
    print("=" * 40)
    print("     PESQUISA DE EQUIPAS (SCOUTING)     ")
    print("=" * 40)
    nome_eq = input("Digite o nome da equipa portuguesa (ex: Sporting, Alverca): ")
    
    resultado = pesquisar_equipa(nome_eq)
    
    if resultado:
        limpar_ecran()
        print("=" * 50)
        print(f" SCOUTING: {resultado['nome'].upper()} ")
        print(f" Competição: {resultado['liga']}")
        print("=" * 50)
        print(f" • Melhor Marcador: {resultado['scout']['melhor_marcador']}")
        print(f" • Perfil/Resumo:   {resultado['scout']['resumo']}")
        print("-" * 50)
        print(" ESTATÍSTICAS NA LIGA:")
        stats = resultado['stats']
        print(f"   Pontos: {stats['P']} | Jogos: {stats['J']}")
        print(f"   Vitórias: {stats['V']} | Empates: {stats['E']} | Derrotas: {stats['D']}")
        print(f"   Golos Marcados: {stats['GM']} | Golos Sofridos: {stats['GS']}")
        print("=" * 50)
    else:
        print("\n❌ Equipa não encontrada no sistema de dados nacional.")
        
    input("\nPressione Enter para voltar...")

def main():
    while True:
        mostrar_menu_principal()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            mostrar_menu_divisao("Liga Portugal")
        elif opcao == "2":
            mostrar_menu_divisao("Liga Portugal 2")
        elif opcao == "3":
            mostrar_menu_divisao("Liga 3")
        elif opcao == "4":
            exibir_pesquisa_scouting()
        elif opcao == "0":
            print("\n Obrigado por usar o TugaScore! A fechar...")
            break
        else:
            print("\n❌ Opção Inválida! Pressione Enter para tentar novamente...")
            input()

if __name__ == "__main__":
    main()