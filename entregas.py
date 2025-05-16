class Entrega:
    _id_counter = 1  # Atributo de classe para controle de ID

    def __init__(self, cidade_destino, centro_origem, distancia, caminhao, prazo, custo, horas_estimadas, peso):
        self.id = Entrega._id_counter
        Entrega._id_counter += 1

        self.cidade_destino = cidade_destino
        self.centro_origem = centro_origem
        self.distancia = distancia
        self.caminhao = caminhao
        self.prazo = prazo
        self.custo = custo
        self.horas_estimadas = horas_estimadas
        self.peso = peso
        self.status = "Em andamento"  # Status padrão

    def detalhes_entrega(self):
        return (f"\n===== DETALHES DA ENTREGA =====\n"
                f"ID: {self.id}\n"
                f"Centro de Distribuição: {self.centro_origem}\n"
                f"Destino: {self.cidade_destino}\n"
                f"Peso da Carga: {self.peso:.2f} kg\n"
                f"Distância: {self.distancia:.2f} km\n"
                f"Caminhão Escolhido: {self.caminhao}\n"
                f"Quantidade de horas Estimado para Entrega: {self.horas_estimadas:.2f} horas\n"
                f"Prazo Estimado: {self.prazo} dias\n"
                f"Custo de Combustível: R$ {self.custo:.2f}\n"
                f"Status da Entrega: {self.status}\n")


# Lista para armazenar todas as entregas
entregas = []