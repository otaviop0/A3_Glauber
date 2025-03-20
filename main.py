import requests
from haversine import haversine
from caminhoes import escolher_caminhao

# Chave da OpenCage API
api_key = "b431b8eeb3bf4c58a5bb82877d41b534"                    ##Key_OP 00ceb07d37a34c7db5abf142fa3b62e2

# Centros de distribuição
centros_distribuicao = {
    "Florianópolis": (-27.5954, -48.5480),
    "Belém": (-1.4558, -48.4903),
    "Recife": (-8.0476, -34.8770),
    "São Paulo": (-23.5505, -46.6333),
    "Brasília": (-15.7801, -47.9292)
}


# Função para pegar coordenadas usando OpenCage API  -- tratamento de exceção adicionado na função da api
def get_coordinates(city):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get('results'):
            latitude = data['results'][0]['geometry']['lat']
            longitude = data['results'][0]['geometry']['lng']
            return (latitude, longitude)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    except (KeyError, IndexError):
        print("Erro ao processar os dados da API.")

    return None


# Função para calcular a distância e encontrar o centro mais próximo
def encontrar_centro_proximo(cidade_origem):
    origem_coords = get_coordinates(cidade_origem)

    if origem_coords is None:
        return None, None

    distancia_minima = float('inf')
    centro_proximo = None

    for centro, coords in centros_distribuicao.items():
        distancia = haversine(origem_coords, coords)
        if distancia < distancia_minima:
            distancia_minima = distancia
            centro_proximo = centro

    return centro_proximo, distancia_minima


# Função principal
def main():
    cidade = input("Digite o nome da cidade de origem para entrega: ")

    while True:
        try:
            peso = float(input("Digite o peso da carga (em kg): "))
            if peso <= 0:
                raise ValueError("O peso deve ser um número positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

    centro, distancia = encontrar_centro_proximo(cidade)
    if centro:
        caminhao, consumo = escolher_caminhao(peso, distancia)
        if caminhao:
            print(f"O centro de distribuição mais próximo de {cidade} é {centro}, a {distancia:.2f} km de distância.")
            print(f"Para essa carga, recomendamos o {caminhao}.")
            print(f"Consumo estimado: {consumo:.2f} litros.")
        else:
            print("Não há caminhões disponíveis para esse peso.")
    else:
        print("Cidade não encontrada.")


# Chama a função principal
if __name__ == "__main__":
    main()