# Algoritmo de Busca A*

## Projeto de Inteligência Artificial - Labirinto A*

Este projeto implementa o algoritmo de busca A* para resolver labirintos.

## Requisitos

- **Ambiente de Desenvolvimento:** Windows
- **Linguagem:** Python 3.11.4

## Bibliotecas Python

Para executar este projeto, instale as seguintes bibliotecas usando o `pip`:

```bash
pip install PyQt5 pickle5
```
Talvez outras bibliotecas sejam necessárias.

## Execução do código

Para executar a aplicação:

```bash
python main.py
```

## Personalização do Labirinto**
   - Clique nos blocos para definir o ponto de partida, o ponto de destino e os blocos intransponíveis.
   - Clique no botão "BUSCAR" para que o algoritmo encontre o caminho entre o ponto de partida e o ponto de destino.
   - Após o processamento, você pode usar o botão "Próximo Caminho" para visualizar todos os caminhos encontrados.

## Como o Algoritmo Funciona

Ao definir um ponto de partida e um ponto de destino, o algoritmo calcula inicialmente as distâncias entre todos os pontos da tabela até o destino. Isso é feito usando o método de Manhattan, que calcula a soma das diferenças entre as coordenadas dos pontos. Em seguida, o algoritmo começa a iteração, especulando sobre os nós adjacentes ao nó atual. Os movimentos são restritos às direções para cima, baixo, esquerda e direita. As opções são ordenadas de acordo com a estimativa de Manhattan, permitindo que o algoritmo explore os caminhos mais promissores primeiro. O algoritmo continua a percorrer os nós até encontrar o destino, armazenando os caminhos percorridos. Se forem encontrados caminhos, eles são exibidos após o processamento.




