# Rotulação de Componentes Conectadas

Atividade da disciplina **Processamento de Imagens** – UFT. Este projeto implementa a rotulação de componentes conectadas em uma imagem binária utilizando conectividade 4, 8 ou mista (condicional). A imagem de entrada é processada para identificar regiões conectadas com base no conjunto de valores desejado (`Cs`), e o resultado é visualizado com cores distintas para cada região. O código utiliza as bibliotecas NumPy e Matplotlib para o processamento e a visualização.

**Aluna:** Laura Barbosa Henrique | **E-mail:** laura.henrique@mail.uft.edu.br

Para executar, certifique-se de ter o Python 3 instalado. Em seguida, instale as dependências necessárias com o comando `pip install numpy matplotlib`. Depois disso, execute o arquivo com `python codigo2pi_laurabh.py`.

**Exemplo de saída:**  
Imagem original:  
[[ 38 255 255 124]  
 [149 255 254 238]  
 [ 30   1 255 255]  
 [255 255   0  98]  
 [ 38 255 255 124]  
 [255 255  60 255]]  

Imagem rotulada (cada número = uma região conectada):  
[[0 1 1 0]  
 [0 1 0 0]  
 [0 0 1 1]  
 [1 1 0 0]  
 [0 1 1 0]  
 [1 1 0 1]]  

O programa também exibe uma visualização colorida das regiões rotuladas usando Matplotlib.
