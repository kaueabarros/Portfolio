import csv
from numpy import RankWarning

from pandas import RangeIndex

class megasena:
    def __init__(self,arquivo,mes,ano,reverso, sequencia = None):        
        with open(arquivo, mode = 'r', newline = '', encoding = 'utf-8') as lista:
            leitor = csv.reader(lista, delimiter = ';') 
            self.conteudo_lista = list(leitor)
        self.mes_referencia = mes
        self.ano_referencia = ano
        self.reverso = reverso
        if sequencia != None:
            self.sequencia = sequencia
    
    def listaranking(self):
        ranking = []
        sequencia = []
        for i in range(1,61,1):
            ranking.append([i,0])
        for lista in self.conteudo_lista:
            for rank in ranking:
                if int(rank[0]) == int(lista[2]) or int(rank[0]) == int(lista[3]) or int(rank[0]) == int(lista[4]) or int(rank[0]) == int(lista[5]) or int(rank[0]) == int(lista[6]) or int(rank[0]) == int(lista[7]):
                    rank[1] = rank[1] + 1
        ranking_ordenado = sorted(ranking,reverse = self.reverso,key=lambda x: x[1]) 
        print('Ranking Geral')
        for i in range(0,6,1):
            print(f'O número {ranking_ordenado[i][0]} aparece {ranking_ordenado[i][1]} vezes')  
            sequencia.append(ranking_ordenado[i][0])          
        print(ranking_ordenado[:6])
        return sorted(sequencia)

    def listarankingmes(self):
        ranking = []
        for i in range(1,61,1):
            ranking.append([i,0])
        for lista in self.conteudo_lista:
            mes = lista[1].split('/')[1]
            for rank in ranking:
                if int(self.mes_referencia) == int(mes):
                    if int(rank[0]) == int(lista[2]) or int(rank[0]) == int(lista[3]) or int(rank[0]) == int(lista[4]) or int(rank[0]) == int(lista[5]) or int(rank[0]) == int(lista[6]) or int(rank[0]) == int(lista[7]):
                        rank[1] = rank[1] + 1
        ranking_ordenado = sorted(ranking,reverse = self.reverso,key=lambda x: x[1]) 
        print('Ranking Mês')
        for i in range(0,6,1):
            print(f'O número {ranking_ordenado[i][0]} aparece {ranking_ordenado[i][1]} vezes')            
        print(ranking_ordenado[:6])

    def listarankingmesano(self):
        ranking = []
        for i in range(1,61,1):
            ranking.append([i,0])
        for lista in self.conteudo_lista:
            mes = lista[1].split('/')[1]
            ano = lista[1].split('/')[2]
            for rank in ranking:
                if int(self.mes_referencia) == int(mes) and int(self.ano_referencia) == int(ano):
                    if int(rank[0]) == int(lista[2]) or int(rank[0]) == int(lista[3]) or int(rank[0]) == int(lista[4]) or int(rank[0]) == int(lista[5]) or int(rank[0]) == int(lista[6]) or int(rank[0]) == int(lista[7]):
                        rank[1] = rank[1] + 1
        ranking_ordenado = sorted(ranking,reverse = self.reverso,key=lambda x: x[1]) 
        print('Ranking Mês/Ano')
        for i in range(0,6,1):
            print(f'O número {ranking_ordenado[i][0]} aparece {ranking_ordenado[i][1]} vezes')            
        print(ranking_ordenado[:6])

    def contagemsequencia(self):
        if self.sequencia == None:
            print('Sequencia não digitada !')
        else:
            ranking = []
            for lista in self.conteudo_lista:
                if int(self.sequencia[0]) == int(lista[2]) and int(self.sequencia[1]) == int(lista[3]) and int(self.sequencia[2]) == int(lista[4]) and int(self.sequencia[3]) == int(lista[5]) and int(self.sequencia[4]) == int(lista[6]) and int(self.sequencia[5]) == int(lista[7]):
                    ranking.append([lista[1]])
            print(f'A sequencia {self.sequencia} apareceu {len(ranking)} vezes')   
            if len(ranking) > 0:
                print(ranking)

    def frequenciasequenciamega(self):
        ranking = []
        for lista in self.conteudo_lista:
            if len(ranking) == 0:
                ranking.append([[lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]],1])
            else:
                achou = False                
                for rank in ranking:
                    if int(rank[0][0]) == int(lista[2]) and int(rank[0][1]) == int(lista[3]) and int(rank[0][2]) == int(lista[4]) and int(rank[0][3]) == int(lista[5]) and int(rank[0][4]) == int(lista[6]) and int(rank[0][5]) == int(lista[7]):
                        rank[1] = rank[1] + 1
                        achou = True
                if achou == False:
                    ranking.append([[lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]],1])
        ranking_ordenado = sorted(ranking,reverse = self.reverso,key=lambda x: x[1])      
        for i in range(0,6,1):   
            print(ranking_ordenado[i][0],' ',ranking_ordenado[i][1])
            
    def frequenciasequenciaquina(self):
        ranking = []
        for lista in self.conteudo_lista:
            if len(ranking) == 0:
                ranking.append([[lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]],1])
            else:
                achou = False                
                for rank in ranking:
                    if int(rank[0][0]) == int(lista[2]) and int(rank[0][1]) == int(lista[3]) and int(rank[0][2]) == int(lista[4]) and int(rank[0][3]) == int(lista[5]) and int(rank[0][3]) == int(lista[6]):
                        rank[1] = rank[1] + 1
                        achou = True
                if achou == False:
                    ranking.append([[lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]],1])
        ranking_ordenado = sorted(ranking,reverse = self.reverso,key=lambda x: x[1])      
        for i in range(0,6,1):   
            print(f' Os números {ranking_ordenado[i][0][0]},{ranking_ordenado[i][0][1]},{ranking_ordenado[i][0][2]},{ranking_ordenado[i][0][3]},{ranking_ordenado[i][0][4]},{ranking_ordenado[i][0][5]} aparecem {ranking_ordenado[i][1]} vezes')

    def frequenciasequenciaquadra(self):
        ranking = []
        for lista in self.conteudo_lista:
            if len(ranking) == 0:
                ranking.append([[lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]],1,[lista[1]]])
            else:
                achou = False                
                for rank in ranking:
                    if int(rank[0][0]) == int(lista[2]) and int(rank[0][1]) == int(lista[3]) and int(rank[0][2]) == int(lista[4]) and int(rank[0][3]) == int(lista[5]):
                        rank[1] = rank[1] + 1
                        rank[2].append(lista[1])
                        achou = True
                if achou == False:
                    ranking.append([[lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]],1,[lista[1]]])                    
        ranking_ordenado = sorted(ranking,reverse = self.reverso,key=lambda x: x[1])      
        for i in range(0,6,1):   
            print(f' Os números {ranking_ordenado[i][0][0]},{ranking_ordenado[i][0][1]},{ranking_ordenado[i][0][2]},{ranking_ordenado[i][0][3]},{ranking_ordenado[i][0][4]} aparecem {ranking_ordenado[i][1]} vezes nos dias {ranking_ordenado[i][2]}')
    
    def sequenciaprovavel(self):
        ranking = self.listaranking()
        self.sequencia = ranking
        self.contagemsequencia()
