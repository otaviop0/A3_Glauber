from geolocalizacao import encontrar_centro_proximo
from entregas import Entrega, entregas
from caminhoes import escolher_caminhao

#Abaixo comando para abrir no terminal e instalar as bibliotecas necessárias
# pip install requests
# pip install haversine


while True:
    print("\n==== MENU ====")
    print("1 - Realizar nova entrega")
    print("2 - Ver entregas realizadas")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cidade_destino = input("Digite a cidade de destino: ")
        
        peso = float(input("Digite o peso da carga (em kg, peso Máximo 14000):"))

        centro, distancia = encontrar_centro_proximo(cidade_destino)

        if centro is None:
            print("Não foi possível localizar a cidade.")
            continue

        caminhao, consumo, prazo, custo, horas_estimadas = escolher_caminhao(centro, peso, distancia)

        if caminhao is not None:
            # Criando uma instância de Entrega com todos os atributos necessários
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