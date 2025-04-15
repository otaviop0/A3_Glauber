import math  # adiciona no topo do arquivo
# Classe que representa um caminhão com seus atributos e métodos relacionados ao transporte

class Caminhao:
    def __init__(self, tipo, peso_maximo, consumo_por_km, velocidade_media, horas_max):
        self.tipo = tipo  # Tipo do caminhão (ex: Van, Toco, Truck)
        self.peso_maximo = peso_maximo  # Capacidade máxima de carga (em kg)
        self.consumo_por_km = consumo_por_km  # Quantidade de combustível gasto por km (litros/km)
        self.velocidade_media = velocidade_media  # Velocidade média do caminhão (km/h)
        self.horas_max = horas_max  # Máximo de horas que o caminhão pode rodar por dia

    def calcular_consumo(self, distancia_km):
        # Calcula o total de combustível consumido com base na distância (litros)
        return distancia_km * self.consumo_por_km

    def calcular_custo_combustivel(self, distancia_km, preco_combustivel=6.00):
        # Calcula o custo total da viagem com base no consumo e no preço do combustível (padrão: R$6,00 por litro)
        consumo_total = self.calcular_consumo(distancia_km)
        return consumo_total * preco_combustivel

    def calcular_prazo(self, distancia_km):
        # Calcula o prazo estimado da entrega em dias com base na distância e tempo de rodagem por dia
        tempo_total_horas = distancia_km / self.velocidade_media
        dias = tempo_total_horas / self.horas_max
        return max(1, math.ceil(dias))  # Garante que o prazo mínimo seja de 1 dia

# Dicionário que representa a quantidade de caminhões disponíveis em cada centro de distribuição
centros_distribuicao_caminhoes = {
    "Florianópolis": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "Belém": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "Recife": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "São Paulo": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2},
    "Brasília": {"Van": 2, "Caminhão Toco (2 eixos)": 2, "Caminhão Truck (3 eixos)": 2}
}

# Lista com os tipos de caminhões disponíveis no sistema, do menor para o maior
# Os valores de consumo são aproximados da realidade:
# Van: 10 km/l → 0.10 l/km
# Toco: 4 km/l → 0.25 l/km
# Truck: 2.5 km/l → 0.40 l/km
caminhoes = [
    Caminhao("Van", 1500, 0.10, 80, 8),                    # Ideal para cargas leves
    Caminhao("Caminhão Toco (2 eixos)", 6000, 0.25, 70, 9), # Médio porte
    Caminhao("Caminhão Truck (3 eixos)", 14000, 0.40, 60, 10)  # Grande porte
]

# Função que seleciona o caminhão ideal de acordo com o peso da carga, disponibilidade e distância
# Também verifica se o peso não excede o limite do maior caminhão
def escolher_caminhao(centro, peso, distancia_km):
    caminhão_selecionado = None  # Tipo do caminhão escolhido
    aviso = ""  # Armazena mensagens de aviso caso algum tipo de caminhão esteja indisponível

    # Verifica se o peso excede o limite do maior caminhão
    maior_peso = max(c.peso_maximo for c in caminhoes)
    if peso > maior_peso:
        print(f"❌ Peso informado ({peso} kg) excede o limite do maior caminhão ({maior_peso} kg).")
        return None, None, None, None, None  

    # Itera sobre a lista de caminhões (do menor para o maior)
    for i, caminhao in enumerate(caminhoes):
        if peso <= caminhao.peso_maximo:
            if centros_distribuicao_caminhoes[centro][caminhao.tipo] > 0:
                caminhão_selecionado = caminhao.tipo
                break
            else:
                if i + 1 < len(caminhoes):
                    proximo = caminhoes[i + 1].tipo
                    aviso += f"\n⚠️ Todos os {caminhao.tipo}s estão ocupados. Tentando {proximo}..."
                else:
                    aviso += f"\n⚠️ Todos os {caminhao.tipo}s estão ocupados."

    if caminhão_selecionado is None:
        print("\n❌ Nenhum caminhão disponível nesse centro de distribuição no momento.")
        return None, None, None, None, None  # Agora retorna 5 valores

    if aviso:
        print(aviso)

    centros_distribuicao_caminhoes[centro][caminhão_selecionado] -= 1
    melhor_caminhao = next(c for c in caminhoes if c.tipo == caminhão_selecionado)

    consumo = melhor_caminhao.calcular_consumo(distancia_km)
    prazo = melhor_caminhao.calcular_prazo(distancia_km)
    custo = melhor_caminhao.calcular_custo_combustivel(distancia_km)
    horas_estimadas =  math.ceil(distancia_km / melhor_caminhao.velocidade_media)  # Cálculo das horas estimadas para a entrega

    return caminhão_selecionado, consumo, prazo, custo, horas_estimadas  
