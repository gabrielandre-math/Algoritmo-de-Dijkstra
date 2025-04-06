def dijkstra(mapa_cidade, origem):
    """
    Implementação do algoritmo de Dijkstra para encontrar o caminho mais curto
    entre cidades considerando o tempo de viagem em minutos.
    """
    # Inicialização dos tempos como infinito para todas as cidades
    tempos = {cidade: float('infinity') for cidade in mapa_cidade}
    # A cidade de origem tem tempo zero
    tempos[origem] = 0
    # Cidades ainda não visitadas
    nao_visitadas = list(mapa_cidade.keys())
    # Para rastrear os caminhos
    rotas = {cidade: [] for cidade in mapa_cidade}
    rotas[origem] = [origem]
    # Para rastrear os meios de transporte usados
    transportes_usados = {cidade: [] for cidade in mapa_cidade}
    
    # Enquanto houver cidades não visitadas
    while nao_visitadas:
        # Encontra a cidade não visitada com menor tempo de viagem
        atual = min(nao_visitadas, key=lambda cidade: tempos[cidade])
        
        # Se o menor tempo for infinito, as cidades restantes são inacessíveis
        if tempos[atual] == float('infinity'):
            break
            
        # Marca a cidade atual como visitada
        nao_visitadas.remove(atual)
        
        # Verifica cada cidade vizinha e atualiza o tempo se encontrar uma rota mais rápida
        for vizinha, dados in mapa_cidade[atual].items():
            tempo = tempos[atual] + dados["tempo"]
            transporte = dados["transporte"]
            
            # Se encontrar uma rota mais rápida, atualiza o tempo e o caminho
            if tempo < tempos[vizinha]:
                tempos[vizinha] = tempo
                rotas[vizinha] = rotas[atual] + [vizinha]
                transportes_usados[vizinha] = transportes_usados.get(atual, []) + [transporte]
    
    return tempos, rotas, transportes_usados

def exibir_resultados_viagem(origem, tempos, rotas, transportes):
    """
    Exibe os resultados da busca de rotas de forma amigável e intuitiva.
    """
    print("\n" + "="*70)
    print(f"🌍 MELHORES ROTAS DE VIAGEM A PARTIR DE {origem.upper()} 🌍")
    print("="*70)
    
    print("\n📊 RESUMO DAS MELHORES ROTAS:")
    print("-"*70)
    print(f"{'DESTINO':<15}{'TEMPO':<15}{'MEIO(S) DE TRANSPORTE':<25}{'ROTA COMPLETA'}")
    print("-"*70)
    
    # Ordena as cidades pelo tempo de viagem (do mais rápido ao mais demorado)
    cidades_ordenadas = sorted(tempos.keys(), key=lambda x: tempos[x] if tempos[x] != float('infinity') else float('inf'))
    
    for cidade in cidades_ordenadas:
        if cidade == origem:
            continue  # Pula a cidade de origem na listagem
            
        tempo = tempos[cidade]
        if tempo == float('infinity'):
            print(f"{cidade:<15}{'Inacessível':<15}{'N/A':<25}{'Não há rota disponível'}")
            continue
            
        # Formatação do tempo em horas e minutos
        horas = tempo // 60
        minutos = tempo % 60
        if horas > 0:
            tempo_formatado = f"{int(horas)}h {int(minutos)}min"
        else:
            tempo_formatado = f"{int(minutos)}min"
            
        # Prepara a representação da rota com emojis para cidades
        rota_emoji = " 🚀 ".join(rotas[cidade])
        
        # Prepara a lista de transportes
        meios_transporte = transportes[cidade]
        icones_transporte = []
        for t in meios_transporte:
            if t == "carro":
                icones_transporte.append("🚗")
            elif t == "trem":
                icones_transporte.append("🚄")
            elif t == "ônibus":
                icones_transporte.append("🚌")
            elif t == "barco":
                icones_transporte.append("⛵")
            elif t == "avião":
                icones_transporte.append("✈️")
            else:
                icones_transporte.append(t)
        
        transporte_str = " → ".join(icones_transporte)
        
        print(f"{cidade:<15}{tempo_formatado:<15}{transporte_str:<25}{rota_emoji}")
    
    print("-"*70)
    print("🕒 Tempos estimados consideram condições normais de tráfego e clima.")
    print("🔄 Rotas calculadas pelo algoritmo de Dijkstra - caminho mais rápido.")
    print("="*70 + "\n")

# Exemplo com cidades brasileiras e diferentes meios de transporte
if __name__ == '__main__':
    # Mapa de cidades como um grafo ponderado, onde o peso é o tempo em minutos
    mapa_brasil = {
        "São Paulo": {
            "Rio de Janeiro": {"tempo": 360, "transporte": "carro"},
            "Belo Horizonte": {"tempo": 480, "transporte": "carro"},
            "Curitiba": {"tempo": 300, "transporte": "carro"},
            "Brasília": {"tempo": 90, "transporte": "avião"}
        },
        "Rio de Janeiro": {
            "São Paulo": {"tempo": 360, "transporte": "carro"},
            "Belo Horizonte": {"tempo": 420, "transporte": "carro"},
            "Vitória": {"tempo": 300, "transporte": "carro"},
            "Salvador": {"tempo": 120, "transporte": "avião"}
        },
        "Belo Horizonte": {
            "São Paulo": {"tempo": 480, "transporte": "carro"},
            "Rio de Janeiro": {"tempo": 420, "transporte": "carro"},
            "Brasília": {"tempo": 360, "transporte": "carro"}
        },
        "Curitiba": {
            "São Paulo": {"tempo": 300, "transporte": "carro"},
            "Florianópolis": {"tempo": 180, "transporte": "carro"},
            "Porto Alegre": {"tempo": 360, "transporte": "ônibus"}
        },
        "Brasília": {
            "São Paulo": {"tempo": 90, "transporte": "avião"},
            "Belo Horizonte": {"tempo": 360, "transporte": "carro"},
            "Goiânia": {"tempo": 180, "transporte": "carro"},
            "Salvador": {"tempo": 90, "transporte": "avião"}
        },
        "Salvador": {
            "Rio de Janeiro": {"tempo": 120, "transporte": "avião"},
            "Brasília": {"tempo": 90, "transporte": "avião"},
            "Recife": {"tempo": 240, "transporte": "carro"}
        },
        "Recife": {
            "Salvador": {"tempo": 240, "transporte": "carro"},
            "Fortaleza": {"tempo": 360, "transporte": "carro"}
        },
        "Fortaleza": {
            "Recife": {"tempo": 360, "transporte": "carro"},
            "Manaus": {"tempo": 210, "transporte": "avião"}
        },
        "Manaus": {
            "Fortaleza": {"tempo": 210, "transporte": "avião"},
            "Belém": {"tempo": 480, "transporte": "barco"}
        },
        "Belém": {
            "Manaus": {"tempo": 480, "transporte": "barco"}
        },
        "Vitória": {
            "Rio de Janeiro": {"tempo": 300, "transporte": "carro"}
        },
        "Goiânia": {
            "Brasília": {"tempo": 180, "transporte": "carro"}
        },
        "Florianópolis": {
            "Curitiba": {"tempo": 180, "transporte": "carro"},
            "Porto Alegre": {"tempo": 240, "transporte": "carro"}
        },
        "Porto Alegre": {
            "Florianópolis": {"tempo": 240, "transporte": "carro"},
            "Curitiba": {"tempo": 360, "transporte": "ônibus"}
        }
    }
    
    # Cidade de origem para o cálculo das rotas
    cidade_origem = "São Paulo"
    
    # Calcula os caminhos mais rápidos
    tempos, rotas, transportes = dijkstra(mapa_brasil, cidade_origem)
    
    # Exibe os resultados de forma intuitiva
    exibir_resultados_viagem(cidade_origem, tempos, rotas, transportes)
