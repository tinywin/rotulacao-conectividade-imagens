# Rotulação de Componentes Conectadas

Atividade da disciplina **Processamento de Imagens** – UFT.

## Sobre

Este projeto implementa a **rotulação de componentes conectadas** em uma imagem binária utilizando conectividade 4, 8 ou mista (condicional). A imagem de entrada é processada para identificar regiões conectadas com base no conjunto de valores desejado (`Cs`), e o resultado é visualizado com cores distintas para cada região.

O código utiliza **NumPy** e **Matplotlib** para processamento e visualização.

## Aluna

- **Nome:** Laura Barbosa Henrique  
- **E-mail:** laura.henrique@mail.uft.edu.br

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Instale as dependências necessárias (caso ainda não tenha):

```bash
pip install numpy matplotlib

3. Execute o arquivo com:



python codigo2pi_laurabh.py

Exemplo de saída

Imagem original:
[[ 38 255 255 124]
 [149 255 254 238]
 [ 30   1 255 255]
 [255 255   0  98]
 [ 38 255 255 124]
 [255 255  60 255]]

Imagem rotulada (cada número = uma região conectada):
[[0 1 1 0]
 [0 1 0 0]
 [0 0 1 1]
 [1 1 0 0]
 [0 1 1 0]
 [1 1 0 1]]

> O programa também exibe uma visualização colorida das regiões rotuladas usando matplotlib.
