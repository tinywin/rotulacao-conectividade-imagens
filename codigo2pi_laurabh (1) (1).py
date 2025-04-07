# Aluna: Laura Barbosa Henrique
# Matrícula: 2022216981
# Código 2 - Rotulação de Componentes Conectadas
# Data: 04/04/2025
# Universidade Federal do Tocantins
# Disciplina: Processamento de Imagens
# Descrição: Rotula regiões conectadas em uma imagem binária e exibe os rótulos com cores.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def binarizar(imagem, Cs):
    return np.isin(imagem, list(Cs)).astype(int)

def rotulacao(imagem_original, conectividade='4', Cs={255}):
    imagem_binaria = binarizar(imagem_original, Cs)
    linhas, colunas = imagem_binaria.shape
    rotulos = np.zeros_like(imagem_binaria, dtype=int)
    rotulo_atual = 1
    equivalencias = {}

    def encontrar_raiz(r):
        while equivalencias[r] != r:
            r = equivalencias[r]
        return r

    def unir(r1, r2):
        raiz1 = encontrar_raiz(r1)
        raiz2 = encontrar_raiz(r2)
        if raiz1 != raiz2:
            equivalencias[raiz2] = raiz1

    def vizinhos_validos(i, j):
        vizinhos = []
        if i > 0 and imagem_binaria[i-1, j] == 1:
            vizinhos.append(((i-1, j), rotulos[i-1, j]))
        if j > 0 and imagem_binaria[i, j-1] == 1:
            vizinhos.append(((i, j-1), rotulos[i, j-1]))
        if conectividade in ['8', 'm']:
            if i > 0 and j > 0 and imagem_binaria[i-1, j-1] == 1:
                if conectividade == '8' or m_condicao(i, j, i-1, j-1):
                    vizinhos.append(((i-1, j-1), rotulos[i-1, j-1]))
            if i > 0 and j < colunas - 1 and imagem_binaria[i-1, j+1] == 1:
                if conectividade == '8' or m_condicao(i, j, i-1, j+1):
                    vizinhos.append(((i-1, j+1), rotulos[i-1, j+1]))
        return [v[1] for v in vizinhos if v[1] != 0]

    def m_condicao(i1, j1, i2, j2):
        n4_p = [(i1-1, j1), (i1, j1-1)]
        n4_q = [(i2-1, j2), (i2, j2-1)]
        for a in n4_p:
            for b in n4_q:
                if a == b and 0 <= a[0] < linhas and 0 <= a[1] < colunas:
                    if imagem_binaria[a[0], a[1]] == 1:
                        return False
        return True

    for i in range(linhas):
        for j in range(colunas):
            if imagem_binaria[i, j] == 1:
                vizinhos = vizinhos_validos(i, j)
                if not vizinhos:
                    rotulos[i, j] = rotulo_atual
                    equivalencias[rotulo_atual] = rotulo_atual
                    rotulo_atual += 1
                else:
                    menor = min(vizinhos)
                    rotulos[i, j] = menor
                    for v in vizinhos:
                        if v != menor:
                            unir(menor, v)

    for i in range(linhas):
        for j in range(colunas):
            if rotulos[i, j] != 0:
                rotulos[i, j] = encontrar_raiz(rotulos[i, j])

    return rotulos

def visualizar_rotulos(rotulada):
    n_rotulos = rotulada.max()
    cores = ['black'] + list(plt.cm.tab20.colors[:n_rotulos])
    cmap = colors.ListedColormap(cores)
    bounds = list(range(n_rotulos + 2))
    norm = colors.BoundaryNorm(bounds, cmap.N)
    plt.figure(figsize=(6, 6))
    plt.imshow(rotulada, cmap=cmap, norm=norm)
    plt.title("Regiões conectadas coloridas (preto = fora de região)")
    plt.colorbar(ticks=range(n_rotulos + 1), label='Rótulos das regiões')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    imagem = np.array([
        [38, 255, 255, 124],
        [149, 255, 254, 238],
        [30,   1, 255, 255],
        [255, 255,   0,  98],
        [38, 255, 255, 124],
        [255, 255,  60, 255]
    ])
    Cs = {255}
    tipo = '8'
    rotulada = rotulacao(imagem, conectividade=tipo, Cs=Cs)
    print("Imagem original:")
    print(imagem)
    print("\nImagem rotulada (cada número = uma região conectada):")
    print(rotulada)
    visualizar_rotulos(rotulada)