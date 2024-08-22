'''Desenvolva um sistema de estoque que possui a Classe produtos com as
seguintes características:
○ Atributos: nome, preco, quantidade e codigo.
○ Métodos: calcular_total, atualizar_preco e verificar_disponibilidade.
'''
class Produto:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def calcular_total(self):
        return self.preco * self.quantidade

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco

    def verificar_disponibilidade(self, quantidade_solicitada):
        return self.quantidade >= quantidade_solicitada
    
produto1 = Produto("Camiseta", 29.99, 10, 1234)

valor_total = produto1.calcular_total()
print("Valor total em estoque:", valor_total)

produto1.atualizar_preco(35.99)

disponivel = produto1.verificar_disponibilidade(5)
print("Produto disponível:", disponivel)