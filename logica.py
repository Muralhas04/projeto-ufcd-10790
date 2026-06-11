# logica.py
from dados import ligas, jogos, scouting_equipas

def calcular_classificacoes():
    """Lê os jogos registados e calcula os pontos, vitórias, golos, etc., de cada equipa."""
    # Reset às estatísticas para não duplicar valores ao recalcular
    for liga in ligas:
        for eq in ligas[liga]:
            ligas[liga][eq] = {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0}

    # Processar os resultados dos jogos para somar pontos
    for liga, jornadas in jogos.items():
        for num_jornada, lista_jogos in jornadas.items():
            for jogo in lista_jogos:
                c = jogo["casa"]
                f = jogo["fora"]
                gc = jogo["g_casa"]
                gf = jogo["g_fora"]

                # Registar jogos e golos
                ligas[liga][c]["J"] += 1
                ligas[liga][f]["J"] += 1
                ligas[liga][c]["GM"] += gc
                ligas[liga][c]["GS"] += gf
                ligas[liga][f]["GM"] += gf
                ligas[liga][f]["GS"] += gc

                # Distribuir pontos (Vitória = 3, Empate = 1)
                if gc > gf:
                    ligas[liga][c]["P"] += 3
                    ligas[liga][c]["V"] += 1
                    ligas[liga][f]["D"] += 1
                elif gf > gc:
                    ligas[liga][f]["P"] += 3
                    ligas[liga][f]["V"] += 1
                    ligas[liga][c]["D"] += 1
                else:
                    ligas[liga][c]["P"] += 1
                    ligas[liga][f]["P"] += 1
                    ligas[liga][c]["E"] += 1
                    ligas[liga][f]["E"] += 1

def obter_tabela_ordenada(nome_liga):
    """Retorna a lista de equipas da liga ordenada por Pontos (P) e Diferença de Golos."""
    calcular_classificacoes()
    dados_liga = ligas[nome_liga]
    
    # Ordena as equipas: primeiro por Pontos (P), depois por saldo de golos (GM - GS)
    equipas_ordenadas = sorted(
        dados_liga.items(),
        key=lambda item: (item[1]["P"], item[1]["GM"] - item[1]["GS"]),
        reverse=True
    )
    return equipas_ordenadas

def pesquisar_equipa(nome_equipa):
    """Procura uma equipa no sistema e devolve o seu resumo de scouting e dados atuais."""
    calcular_classificacoes()
    nome_procurado = nome_equipa.strip().lower()
    
    for liga, equipas in ligas.items():
        for eq, stats in equipas.items():
            if eq.lower() == nome_procurado:
                info_scout = scouting_equipas.get(eq, {"melhor_marcador": "N/A", "resumo": "Sem dados de scouting disponíveis."})
                return {
                    "nome": eq,
                    "liga": liga,
                    "stats": stats,
                    "scout": info_scout
                }
    return None