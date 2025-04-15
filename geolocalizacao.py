cidades_destino = [
    "Manaus", "Porto Velho", "Sao Luis",            # Norte
    "Salvador", "Fortaleza", "Joao Pessoa",       # Nordeste
    "Goiania", "Campo Grande", "Cuiaba",          # Centro-Oeste
    "Rio De Janeiro", "Belo Horizonte", "Vitoria",# Sudeste
    "Curitiba", "Porto Alegre", "Caxias Do Sul"   # Sul
]

# Dicionário com distâncias reais aproximadas entre cidades e CDs
distancias_reais = {
    "Manaus": {
        "Belém": 1600,
        "Recife": 3500,
        "Brasília": 3900,
        "São Paulo": 4300,
        "Florianópolis": 4900
    },
    "Porto Velho": {
        "Belém": 2800,
        "Recife": 4100,
        "Brasília": 2500,
        "São Paulo": 2800,
        "Florianópolis": 3300
    },
    "Sao Luis": {
        "Belém": 212,   
        "Recife": 1700, 
        "Brasília": 2300, 
        "São Paulo": 2600, 
        "Florianópolis": 3100
    },
    "Salvador": {
        "Belém": 2100,
        "Recife": 800,
        "Brasília": 1450,
        "São Paulo": 2000,
        "Florianópolis": 2600
    },
    "Fortaleza": {
        "Belém": 1600,
        "Recife": 800,
        "Brasília": 2200,
        "São Paulo": 3100,
        "Florianópolis": 3700
    },
    "Joao Pessoa": {
        "Belém": 1800,
        "Recife": 120,
        "Brasília": 2150,
        "São Paulo": 2600,
        "Florianópolis": 3100
    },
    "Goiania": {
        "Belém": 1800,
        "Recife": 2100,
        "Brasília": 200,
        "São Paulo": 900,
        "Florianópolis": 1600
    },
    "Campo Grande": {
        "Belém": 2600,
        "Recife": 2900,
        "Brasília": 1130,
        "São Paulo": 1000,
        "Florianópolis": 1300
    },
    "Cuiaba": {
        "Belém": 2300,
        "Recife": 2900,
        "Brasília": 1150,
        "São Paulo": 1600,
        "Florianópolis": 2000
    },
    "Rio De Janeiro": {
        "Belém": 2800,
        "Recife": 2500,
        "Brasília": 1200,
        "São Paulo": 440,
        "Florianópolis": 1100
    },
    "Belo Horizonte": {
        "Belém": 2400,
        "Recife": 2100,
        "Brasília": 740,
        "São Paulo": 600,
        "Florianópolis": 1700
    },
    "Vitoria": {
        "Belém": 2500,
        "Recife": 2200,
        "Brasília": 1230,
        "São Paulo": 880,
        "Florianópolis": 1500
    },
    "Curitiba": {
        "Belém": 2800,
        "Recife": 2600,
        "Brasília": 1500,
        "São Paulo": 400,
        "Florianópolis": 300
    },
    "Porto Alegre": {
        "Belém": 3800,
        "Recife": 3600,
        "Brasília": 2500,
        "São Paulo": 1100,
        "Florianópolis": 470
    },
    "Caxias Do Sul": {
        "Belém": 3900,
        "Recife": 3700,
        "Brasília": 2600,
        "São Paulo": 1200,
        "Florianópolis": 460
    }
}

# Função para encontrar o centro de distribuição mais próximo
def encontrar_centro_proximo(cidade_destino):
    if cidade_destino not in distancias_reais:
        return "Sem dados", 0

    distancias = distancias_reais[cidade_destino]  # Pega o dicionário de distâncias entre essa cidade e todos os centros
    centro_proximo = min(distancias, key=distancias.get) # Encontra o centro com a menor distância usando a função min()
    distancia_minima = distancias[centro_proximo]     # Armazena a menor distância encontrada

    return centro_proximo, distancia_minima # Retorna o nome do centro mais próximo e a distância até ele

# Exibe as cidades disponíveis apenas uma vez (opcional)
if __name__ == "__main__":
    cidades_disponiveis = [cidade for cidade in cidades_destino if cidade in distancias_reais]
    print("Cidades destinos disponíveis:", ", ".join(cidades_disponiveis))
