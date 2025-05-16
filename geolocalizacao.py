# Classe Grafo que representa um grafo direcionado com pesos
class Grafo:
    def __init__(self):
        self.vertices = {}  # Dicionário onde cada chave é uma cidade de origem e o valor é outro dicionário com os destinos e seus pesos

    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.vertices:
            self.vertices[origem] = {}  # Cria a entrada se a cidade de origem ainda não existe
        self.vertices[origem][destino] = peso  # Adiciona a cidade de destino e a distância (peso)

    def vizinhos(self, origem):
        return self.vertices.get(origem, {})  # Retorna os destinos possíveis a partir da cidade de origem


# Lista com as cidades de destino utilizadas no projeto (incluindo Natal)
cidades_destino = [
    "Manaus", "Porto Velho", "Sao Luis",            # Norte
    "Salvador", "Fortaleza", "Joao Pessoa", "Natal",  # Nordeste (Natal incluída)
    "Goiania", "Campo Grande", "Cuiaba",            # Centro-Oeste
    "Rio De Janeiro", "Belo Horizonte", "Vitoria",  # Sudeste
    "Curitiba", "Porto Alegre", "Caxias Do Sul"     # Sul
]

# Instancia o grafo
grafo = Grafo()

# Dicionário com as distâncias reais das cidades de destino até os centros de distribuição
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
    "Natal": {
        "Belém": 2000,
        "Recife": 350,
        "Brasília": 2100,
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

# Adiciona cada aresta (cidade -> centro de distribuição com distância) ao grafo
for cidade, centros in distancias_reais.items():
    for centro, distancia in centros.items():
        grafo.adicionar_aresta(cidade, centro, distancia)

# Função que retorna o centro de distribuição mais próximo de uma cidade de destino
def encontrar_centro_proximo(cidade_destino):
    if cidade_destino not in grafo.vertices:
        return "Sem dados", 0  # Retorna mensagem padrão se a cidade não tiver dados

    distancias = grafo.vizinhos(cidade_destino)  # Obtém todos os centros e distâncias
    if not distancias:
        return "Sem centros disponíveis", 0

    centro_proximo = min(distancias, key=distancias.get)  # Centro com menor distância
    distancia_minima = distancias[centro_proximo]
    return centro_proximo, distancia_minima  # Retorna o centro mais próximo e a distância

# Código de teste: exibe as cidades de destino que têm dados no grafo
if __name__ == "__main__":
    cidades_disponiveis = [cidade for cidade in cidades_destino if cidade in grafo.vertices]
    print("Cidades destinos disponíveis:", ", ".join(cidades_disponiveis))

    # Exemplo de teste para Natal
    centro, distancia = encontrar_centro_proximo("Natal")
    print(f"Centro mais próximo de Natal: {centro} a {distancia} km")
