class Entrega:
    def __init__(self, cidade_destino, centro_origem, distancia, caminhao, prazo, custo, horas_estimadas, peso):
        self.cidade_destino = cidade_destino
        self.centro_origem = centro_origem
        self.distancia = distancia
        self.caminhao = caminhao
        self.prazo = prazo
        self.custo = custo  # Novo atributo: custo da entrega em R$
        self.horas_estimadas = horas_estimadas  # Novo atributo: horas estimadas
        self.peso = peso  # Novo atributo: peso da carga

    def detalhes_entrega(self):
        return (f"\n===== DETALHES DA ENTREGA =====\n"
                f"Centro de Distribuição: {self.centro_origem}\n"
                f"Destino: {self.cidade_destino}\n"
                f"Peso da Carga: {self.peso:.2f} kg\n"
                f"Distância: {self.distancia:.2f} km\n"
                f"Caminhão Escolhido: {self.caminhao}\n"
                f"Quantidade de horas Estimado para Entrega: {self.horas_estimadas:.2f} horas\n"
                f"Prazo Estimado: {self.prazo} dias\n"
                f"Custo de Combustível: R$ {self.custo:.2f}\n"
                )  # Exibe o peso da carga

# Lista para armazenar todas as entregas
entregas = []