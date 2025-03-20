# caminhoes.py
class Caminhao:
    def __init__(self, tipo, modelo, marca, peso_maximo, consumo_km_l):
        self.tipo = tipo
        self.modelo = modelo
        self.marca = marca
        self.peso_maximo = peso_maximo
        self.consumo_km_l = consumo_km_l

    def calcular_consumo(self, distancia_km):
        return distancia_km / self.consumo_km_l

    # metodo adicionado na classe para como os objetos desta classe devem ser convertidos para string
    def __str__(self):
        return f"{self.tipo} ({self.marca} {self.modelo})"


# Lista de caminhões disponíveis            ##Op:adicionei médias de consumo, capacidade total de carga de veiculos
CAMINHOES = [
    Caminhao("Van", "Sprinter", "Mercedes-Benz", 2350, 8.5),
    Caminhao("Caminhão Médio", "Delivery-11.180", "Volkswagen", 7480, 5.1),
    Caminhao("Carreta", "R 450 Plus", "Scania", 18600, 2.11)
]


# Função para escolher o caminhão mais adequado para o peso inserido
def escolher_caminhao(peso, distancia_km):
    for caminhao in sorted(CAMINHOES, key=lambda c: c.peso_maximo):
        if peso <= caminhao.peso_maximo:
            consumo = caminhao.calcular_consumo(distancia_km)
            return caminhao, consumo
    return None, 0