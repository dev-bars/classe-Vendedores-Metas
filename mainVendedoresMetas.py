#Criei a classe Vendedor, que contem os atributos necessários para o cadastro de um novo vendedor e do valor de suas vendas.
#Esta classe recebe os atributos nome e vendas.

class Vendedor():
    def __init__(self, nome, vendas):
        self.nome = nome
        self.vendas = vendas
#Já o construtor, efetua uma função para identificar se os vendedores bateram a meta ou não.

    def metaDefinida(self, meta):
        if self.vendas >= meta:
            print(f"{self.nome} Bateu a meta")
        else:
            print(f"{self.nome} Não bateu a meta")

#Variaveis criadas sendo cada um dos vendedores da loja            
vendedor1 = Vendedor("Marcos", 1000)
vendedor1.metaDefinida(500)


vendedor2 = Vendedor("Beatriz", 300)
vendedor2.metaDefinida(500)

#Paraa saída de dados, são pelos dados indicados retornam o resultado do if/else conforme definição correspondente.

#1° Membro - Atributos
#2° Membro - Propriedades
#3° Membro - Construtor
#4° Membro - Metodos


    