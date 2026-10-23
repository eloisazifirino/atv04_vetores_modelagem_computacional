
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# CALCULO DO PRODUTO MISTO E DOS VOLUMES

def calcular_volumes(u, v, w):
    u = np.array(u, dtype=float)
    v = np.array(v, dtype=float)
    w = np.array(w, dtype=float)

    if any(vetor.shape != (3,) for vetor in (u, v, w)):
        raise ValueError("Cada vetor deve possuir exatamente 3 coordenadas.")

    produto_misto = np.dot(u, np.cross(v, w))

    volume_paralelepipedo = abs(produto_misto)
    volume_tetraedro = volume_paralelepipedo / 6

    return produto_misto, volume_paralelepipedo, volume_tetraedro


#  LEITURA DOS VETORES PELO TECLADO

def ler_vetor(nome):
    while True:
        entrada = input(
            f"Digite as 3 coordenadas do vetor {nome}, separadas por virgula: "
        )

        try:
            coordenadas = [
                float(valor.strip())
                for valor in entrada.split(",")
            ]

            if len(coordenadas) != 3:
                print("Erro: digite exatamente 3 coordenadas.")
                continue

            return np.array(coordenadas, dtype=float)

        except ValueError:
            print("Entrada invalida. Exemplo: 3, 0, 0")


# cONFIGURACAO DOS GRAFICOS 3D

def configurar_grafico(ax, vertices, titulo):
    vertices = np.array(vertices, dtype=float)

    ax.set_title(titulo)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    minimo = min(vertices.min(), 0)
    maximo = max(vertices.max(), 1)

    centro = (minimo + maximo) / 2
    raio = (maximo - minimo) / 2 + 0.5

    ax.set_xlim(centro - raio, centro + raio)
    ax.set_ylim(centro - raio, centro + raio)
    ax.set_zlim(centro - raio, centro + raio)

    ax.set_box_aspect((1, 1, 1))


# VISUALIZACAO DOS SOLIDOS EM 3D

def visualizar_solidos(u, v, w):
    origem = np.array([0.0, 0.0, 0.0])

    # Vertices do paralelepipedo
    vertices_p = [
        origem,
        u,
        v,
        w,
        u + v,
        u + w,
        v + w,
        u + v + w
    ]

    faces_p = [
        [0, 1, 4, 2],
        [3, 5, 7, 6],
        [0, 1, 5, 3],
        [2, 4, 7, 6],
        [0, 2, 6, 3],
        [1, 4, 7, 5]
    ]

    # Vertices do tetraedro
    vertices_t = [origem, u, v, w]

    faces_t = [
        [0, 1, 2],
        [0, 1, 3],
        [0, 2, 3],
        [1, 2, 3]
    ]

    fig = plt.figure(figsize=(12, 5))

    # Grafico do paralelepipedo
    ax1 = fig.add_subplot(121, projection="3d")

    faces_paralelepipedo = [
        [vertices_p[i] for i in face]
        for face in faces_p
    ]

    ax1.add_collection3d(
        Poly3DCollection(
            faces_paralelepipedo,
            alpha=0.3,
            edgecolor="black"
        )
    )

    configurar_grafico(
        ax1,
        vertices_p,
        "Paralelepipedo"
    )

    # Grafico do tetraedro
    ax2 = fig.add_subplot(122, projection="3d")

    faces_tetraedro = [
        [vertices_t[i] for i in face]
        for face in faces_t
    ]

    ax2.add_collection3d(
        Poly3DCollection(
            faces_tetraedro,
            alpha=0.3,
            edgecolor="black"
        )
    )

    configurar_grafico(
        ax2,
        vertices_t,
        "Tetraedro"
    )

    plt.tight_layout()
    plt.show()


# TESTES MATEMATICOS

def executar_testes():
    print("\n --> TESTES MATEMATICOS <--")

    # Teste 1: volume conhecido
    u = [3, 0, 0]
    v = [0, 4, 0]
    w = [1, 1, 5]

    produto, volume_p, volume_t = calcular_volumes(u, v, w)

    assert np.isclose(produto, 60)
    assert np.isclose(volume_p, 60)
    assert np.isclose(volume_t, 10)

    print("Teste 1 aprovado: calculo dos volumes.")

    # Teste 2: vetores coplanares
    u = [1, 0, 0]
    v = [0, 1, 0]
    w = [1, 1, 0]

    produto, volume_p, volume_t = calcular_volumes(u, v, w)

    assert np.isclose(produto, 0)
    assert np.isclose(volume_p, 0)
    assert np.isclose(volume_t, 0)

    print("Teste 2 aprovado: vetores coplanares.")

    # Teste 3: troca de dois vetores
    u = [3, 0, 0]
    v = [0, 4, 0]
    w = [1, 1, 5]

    produto_original, volume_original, _ = calcular_volumes(u, v, w)

    produto_trocado, volume_trocado, _ = calcular_volumes(u, w, v)

    assert np.isclose(produto_trocado, -produto_original)
    assert np.isclose(volume_trocado, volume_original)

    print("Teste 3 aprovado: troca de vetores.")

    print("Todos os testes foram aprovados!")


def main():
    executar_testes()

    print("\n --> CALCULADORA DE VOLUMES 3D <--")
    print("Informe as coordenadas dos tres vetores.")

    u = ler_vetor("u")
    v = ler_vetor("v")
    w = ler_vetor("w")

    produto, volume_p, volume_t = calcular_volumes(u, v, w)

    print("\n-- RESULTADOS ---")
    print(f"Produto misto: {produto:.2f}")
    print(f"Volume do paralelepipedo: {volume_p:.2f}")
    print(f"Volume do tetraedro: {volume_t:.2f}")

    if np.isclose(volume_p, 0):
        print("\nOs vetores sao linearmente dependentes.")
        print("O solido nao possui volume tridimensional positivo.")
    else:
        print("\nOs vetores sao linearmente independentes.")
        print("O volume tridimensional e positivo.")

    visualizar_solidos(u, v, w)


if __name__ == "__main__":
    main()
