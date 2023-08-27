import math
import sys

from Utils import broadcast
class AStar_script:

    states = {'DEFAULT': 0, "BLOCKED": 1, "START": 2, "END": 3}
    broadcast = broadcast.Broadcast()


    # Função que gera uma tabela vazia
    def createTable(self):

        self.table = []

        for linha in range(0, 5):

            self.table.append([])

            for coluna in range(0, 6):

                text = str(linha) + "," + str(coluna)
                config = {'STATE': "DEFAULT", "ROW": linha, "COL": coluna, "TEXT": text, "DTT": None}
                # STATE = Possíveis estados de um bloco
                # ROW   = Índice da linha onde está o bloco
                # COL   = Índice da coluna onde está o bloco
                # TEXT  = Recebe a linha e a coluna no formato de texto ( para uso gráfico )
                # DTT   = Distance to Target, recebe o valor da distância até o bloco de destino

                self.table[linha].append(config)

        # Armazena o objeto em formato de arquivo
        self.broadcast.saveMap(self.table)


    def calculateA(self, currentStart, currentEnd):

        # Obtém a tabela modificada pelo usuário
        self.table = self.broadcast.saveMap()

        # Nó de início e nó alvo
        self.currentEnd = currentEnd
        self.currentStart = currentStart

        # Dicionário que irá armazenar os caminho encontrados e a contagem
        self.ways = {}
        self.wayCount = 0

        # Quando um caminho for encontrado, o target assume o valor do nó final
        # e a variável de menor custo assume o custo daquele trajeto
        self.target = None
        self.minCost = sys.maxsize

        # Armazena os dados das iterações
        self.tree = {}
        self.visited = {}


        # Configura o nó de origem para a primeira iteração
        key = str(self.currentStart[0]) + "," + str(self.currentStart[1])
        self.tree[key] = {"PARENT": None, "CURRENT": self.currentStart, 'TOTAL': 0, "CHILD": [], "DTT": self.table[self.currentStart[0]][self.currentStart[1]]["DTT"]}
        self.visited[key] = key
        self.__openTree(self.tree[key])


        # Salva os caminhos encontrados
        self.broadcast.waysMap(self.ways)



    def __openTree(self, header):

            # Recebe o a ser visitado
            position = header["CURRENT"]

            # linha de cima
            childs = []

            # Especula os nós adjacentes
            childs.append([position[0] + 1, position[1]]) # Acima
            childs.append([position[0], position[1] + 1]) # Avança para a direira
            childs.append([position[0] - 1, position[1]]) # Abaixo
            childs.append([position[0], position[1] - 1]) # Avança para a esquerda


            childs2 = {}

            # Salva a posição do nó pai
            if header["PARENT"] != None:
                parent = header["PARENT"]["CURRENT"]
            else:
                parent = None

            # Faz um teste de validade nos nós especulados
            count = 0
            for index in range(0, len(childs)):

                # Linha e coluna dos nós
                row = childs[index][0]
                col = childs[index][1]

                key = [row, col]
                key2 = str(row) + "," + str(col)

                # Verifica se o nó está dentro dos limites da tabela                           # Impede que abra o nó pai e impede que abra um nó que já está aberto
                if row >= 0 and row < len(self.table) and col >=0 and col < len(self.table[0]) and key != parent and not key2 in self.visited:

                    # Obém o valor da hipotenusa do nó, como pode haver valores iguais, na chave adiciona-se o valor da linha e coluna
                    try:
                        item = self.table[row][col]
                        childs2[str((item["DTT"]))+str(row)+str(col)] = item
                    except:
                        childs2[str(sys.maxsize)] = None
                else:
                    # Quando um nó está fora do escopo da tabela, ele passa a ter o valor máximo, assim, nunca será aberto
                    childs2[str(sys.maxsize)] = None

            # A função ordena as chaves de distância do menor para o maior
            keys = sorted(childs2.keys())

            # O nó pai recebe o vetor de nós filhos
            header["CHILD"] = childs2


            # Teste de todos os nós filhos descobertos
            for key in keys:

                # se o filho for válido
                if childs2[key] != None:

                    # Obtém o endereço do nó filho visitado
                    id = [childs2[key]["ROW"], childs2[key]["COL"]]

                    # Se não for um bloco bloqueado pelo usuário
                    if self.table[childs2[key]["ROW"]][childs2[key]["COL"]]["STATE"] != 'BLOCKED':

                        # Testa para verificar se a posição testada é o destino, se ainda não for, avança
                        if id != self.currentEnd:

                            # Obtém a somatória do custo estimado gasto até agora ( somatório das hipotenusas )
                            cost = childs2[key]["DTT"] + header["TOTAL"]

                            # Se o valor for menor ou igual ao valor corrente do caminho já encontrado, então abre o nó
                            if cost <= self.minCost:

                                # Insere o nó na árvore de de busca
                                self.tree[childs2[key]["TEXT"]] = {"PARENT": header, "CURRENT": id, 'TOTAL': childs2[key]["DTT"] + header["TOTAL"], "CHILD": [], "DTT": childs2[key]["DTT"] }
                                print("STEP ", childs2[key]["TEXT"], " - ",  childs2[key]["DTT"], "GASTO", self.tree[childs2[key]["TEXT"]]['TOTAL'])

                                # Adiciona o nó que será aberto na lista de nós que já estão abertos - Isso evita loop
                                # Pois isso impede que ele seja aberto por outro nó antes que todos os seus nós adjacentes sejam visitados
                                self.visited[childs2[key]["TEXT"]] = childs2[key]["TEXT"]

                                # Entra na recursão
                                self.__openTree(self.tree[childs2[key]["TEXT"]])
                            else:
                                # Caso o custo de seguir andiante seja maior que de algum caminho já encotrado, ele sobe na árvore
                                print(childs2[key]["TEXT"], cost, "RETORNA")
                        else:

                            # Adiciona o nó na árvore de caminho
                            self.tree[childs2[key]["TEXT"]] = {"PARENT": header, "CURRENT": id, 'TOTAL': childs2[key]["DTT"] + header["TOTAL"], "CHILD": []}

                            # indexa o nó como alvo
                            self.target = childs2[key]["TEXT"]
                            self.minCost = header["TOTAL"]

                            print("Encontrado", header["TOTAL"])

                            # Salva o caminho encontrado no vetor de caminhos possíveis
                            self.__buildWay(self.tree[self.target])
                            self.wayCount = self.wayCount + 1

            # Ao fim da iteração dos nós filhos de um nó, o nó pai é removido da lista de nós abertos, e pode ser novamente visitado por outra
            # sequencia de busca
            currentKey = str(header["CURRENT"][0]) + "," + str(header["CURRENT"][1])
            if currentKey in self.visited:
                del self.visited[currentKey]

            # Sobe na árvore
            print("RETORNA")




    # Sempre que um caminho é encontrado, a recursão a abaixo faz o caminho inverso
    # para salavar a sequência
    def __buildWay(self, node):


        if not self.wayCount in self.ways:
            self.ways[self.wayCount] = []

        if node["PARENT"] != None:
            #print(item["CURRENT"])
            self.ways[self.wayCount].append(node["CURRENT"])
            self.__buildWay(node["PARENT"])



    
    def pitagoras_(self, currentBloc, destBloc ):


                cateto_a =  abs(destBloc["ROW"] - currentBloc["ROW"])
                cateto_b =  abs(destBloc["COL"] - currentBloc["COL"])

                cateto_a = math.pow(cateto_a, 2)
                cateto_b = math.pow(cateto_b, 2)

                distance = math.sqrt(cateto_b + cateto_a)

                currentBloc["DTT"] = distance
                
    # Calcula a distância entre um dado bloco e o bloco de destino, o método da Distância de Manhattan
    def manhattan(self, currentBloc, destBloc ):


                dif_x =  abs(destBloc["ROW"] - currentBloc["ROW"])
                dif_y =  abs(destBloc["COL"] - currentBloc["COL"])


                distance = dif_x + dif_y

                currentBloc["DTT"] = distance




'''abt = AStar_script()
abt.createTable()'''