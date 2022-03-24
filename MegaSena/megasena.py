import csv

from pandas import RangeIndex

class megasena:
    def __init__(self,arquivo,mes,ano,reverso):        
        with open(arquivo, mode = 'r', newline = '', encoding = 'utf-8') as lista:
            leitor = csv.reader(lista, delimiter = ';') 
            self.conteudo_lista = list(leitor)
        self.mes_referencia = mes
        self.ano_referencia = ano
        self.reverso = reverso
    
    def listaranking(self):
        ranking = []
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
        print(ranking_ordenado[:6])

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
