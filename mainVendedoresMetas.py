class Vendedor():
    def __init__(self, nome):
        self.nome = nome

    def vendasRealizadas(self, vendas):
        self.vendasRealizadas = vendas
    
    def metaDefinida(self, meta):
        if self.vendasRealizadas >= meta:
            print(f"{self.nome} Bateu a meta")
        else:
            print(f"{self.nome} Não bateu")

#Variaveis criadas sendo cada um dos vendedores da loja            
vendedor1 = Vendedor("Marcos")
vendedor1.vendasRealizadas(1000)
vendedor1.metaDefinida(500)


vendedor2 = Vendedor("Beatriz")
vendedor2.vendasRealizadas(400)
vendedor2.metaDefinida(500)


#1° Membro - Atributos
#2° Membro - Propriedades
#3° Membro - Construtor
#4° Membro - Metodos


    