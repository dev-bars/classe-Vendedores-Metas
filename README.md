
🚀 Funcionamento do Sistema de Vendedores em Python<br> 
O projeto utiliza a programação orientada a objetos (POO) em Python para modelar a classe "Vendedor", com dois atributos necessários para o cadastro de um novo vendedor: Nome e Valor de suas vendas
permitindo o rastreamento individual de suas vendas e a verificação automática do atingimento de metas.

💻 Estrutura da Classe Vendedor>
A classe Vendedor é composta por dois elementos principais: o construtor (__init__) para inicialização dos dados e um método (metaDefinida) para processamento de lógica.<br><br>
<img src="https://github.com/dev-bars/classe-Vendedores-Metas/blob/Master/classeVendedoresMeta.PNG"><br>

1. 
Construtor: def __init__(self, nome, vendas)Função: É o ponto de entrada para a criação de um novo objeto Vendedor.
Parâmetros de Entrada:nome (string): O nome do vendedor.vendas (numérico): O valor total das vendas realizadas.

Resultado: Ao ser chamado, ele cria uma instância com os atributos self.nome e self.vendas definidos.AtributoDescriçãoself.nomeIdentificação do vendedor.self.vendasTotal de vendas registradas (dado de entrada).2. Método: def metaDefinida(self, meta)Função: Avalia se o vendedor atingiu ou superou uma meta de vendas preestabelecida.Parâmetro de Entrada:meta (numérico): O valor da meta a ser verificada.Lógica: Compara o valor de self.vendas com o valor de meta.Resultado: Imprime uma mensagem (Bateu a meta ou Não bateu a meta) no console, informando o resultado da avaliação para o vendedor.💡 Exemplo de UsoPara utilizar a classe, basta criar uma instância e, em seguida, chamar o método de avaliação:Python# 1. Cria o objeto Vendedor (chamando __init__)
vendedor1 = Vendedor("Joao", 1000)

2.
Avalia a meta (chamando metaDefinida)
vendedor1.metaDefinida(500) 
Exemplo de Saída: Joao Bateu a meta


Este sistema permite uma gestão clara e modular das informações de vendas. <br>
<br>
Como alguns sabem, estou estudando Desenvolvimento de Sistemas e aplicando os novos conhecimentos aos códigos que estou desenvolvendo<br>
