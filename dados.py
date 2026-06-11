# dados.py

# Estrutura principal que guarda as equipas e as suas estatísticas por divisão
ligas = {
    "Liga Portugal": {
        "Sporting": {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "FC Porto": {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Benfica":  {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Braga":    {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0}
    },
    "Liga Portugal 2": {
        "Paços de Ferreira": {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Marítimo":          {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Leixões":           {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Chaves":            {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0}
    },
    "Liga 3": {
        "Fafe":             {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Belenenses":       {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Académica":        {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0},
        "Varzim":           {"P": 0, "J": 0, "V": 0, "E": 0, "D": 0, "GM": 0, "GS": 0}
    }
}

# Histórico de jogos por Jornada e Divisão com os detalhes reais/estáticos
jogos = {
    "Liga Portugal": {
        1: [
            {
                "casa": "Sporting", "fora": "FC Porto", "g_casa": 2, "g_fora": 1,
                "detalhes": {
                    "golos": [("Sporting", "Suarez", 34), ("Sporting", "Pote", 60), ("FC Porto", "Samu", 82)],
                    "cartoes": [("FC Porto", "Varela", "Amarelo", 45)]
                }
            },
            {
                "casa": "Benfica", "fora": "Braga", "g_casa": 1, "g_fora": 1,
                "detalhes": {
                    "golos": [("Benfica", "Pavlidis", 12), ("Braga", "Horta", 75)],
                    "cartoes": [("Benfica", "Otamendi", "Amarelo", 88)]
                }
            }
        ]
    },
    "Liga Portugal 2": {
        1: [
            {
                "casa": "Marítimo", "fora": "Leixões", "g_casa": 0, "g_fora": 0,
                "detalhes": {"golos": [], "cartoes": []}
            }
        ]
    },
    "Liga 3": {
        1: [
            {
                "casa": "Fafe", "fora": "Académica", "g_casa": 3, "g_fora": 0,
                "detalhes": {
                    "golos": [("Fafe", "Picas", 10), ("Fafe", "Picas", 54), ("Fafe", "Carlos", 80)],
                    "cartoes": []
                }
            }
        ]
    }
}

# Dados de scouting para a funcionalidade de Pesquisa de Equipas
scouting_equipas = {
    "Sporting": {"melhor_marcador": "Suarez (1 golo)", "resumo": "Candidato ao título, focado em transições rápidas."},
    "FC Porto": {"melhor_marcador": "Samu (1 golo)", "resumo": "Equipa em reestruturação, forte defensivamente."},
    "Benfica": {"melhor_marcador": "Pavlidis (1 golo)", "resumo": "Estilo de posse de bola, à procura de consistência."},
    "Braga": {"melhor_marcador": "Horta (1 golo)", "resumo": "Equipa muito perigosa no ataque continuado."},
    "Fafe": {"melhor_marcador": "Picas (2 golos)", "resumo": "Forte candidato à subida na Liga 3."}
}