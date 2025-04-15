from geolocalizacao import encontrar_centro_proximo, cidades_destino
from entregas import Entrega, entregas
from caminhoes import escolher_caminhao

# Função para exibir as cidades disponíveis para entrega
def exibir_cidades_disponiveis():
    print("\n" * 2) 
    print("Cidades disponíveis para entrega:", end=" ")
    print(", ".join(cidades_destino))

while True:
    # Exibe as cidades disponíveis para entrega
    exibir_cidades_disponiveis()
    
    print("\n==== MENU ====")
    print("1 - Realizar nova entrega")
    print("2 - Ver entregas realizadas")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            cidade_destino = input("Digite a cidade de destino: ").strip().title()
            if cidade_destino in cidades_destino:
                break
            else:
                print("Cidade inválida. Escolha entre:", ", ".join(cidades_destino))

        peso = float(input("Digite o peso da carga (em kg, peso máximo 14000): "))

        centro, distancia = encontrar_centro_proximo(cidade_destino)

        if centro is None:
            print("Não foi possível localizar a cidade.")
            continue

        caminhao, consumo, prazo, custo, horas_estimadas = escolher_caminhao(centro, peso, distancia)

        if caminhao is not None:
            entrega = Entrega(cidade_destino, centro, distancia, caminhao, prazo, custo, horas_estimadas, peso)
            entregas.append(entrega)
            print(entrega.detalhes_entrega())

    elif opcao == "2":
        if not entregas:
            print("Nenhuma entrega registrada.")
        else:
            for entrega in entregas:
                print(entrega.detalhes_entrega())

    elif opcao == "0":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida. Tente novamente.")
