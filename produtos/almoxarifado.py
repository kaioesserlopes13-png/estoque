# produtos/almoxarifado.py — a classe Almoxarifado guarda os produtos de uma unidade
class Almoxarifado:
# Construtor: o almoxarifado nasce com o nome da unidade e sem produtos
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []
        # Guarda um objeto Produto no fim da lista
    def adicionar(self, produto):
        self.produtos.append(produto)

    def buscar(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def entrada(self, codigo, qtd):
        produto = self.buscar(codigo)

        if produto is None:
            return False

        produto.entrada(qtd)
        return True

    def saida(self, codigo, qtd):
        produto = self.buscar(codigo)

        if produto is None:
            return False

        return produto.saida(qtd)

    def listar(self):
        lista = []

        for produto in self.produtos:
            lista.append(produto.listar_produtos())

        return lista

    def solicitacao_compra(self):
        pedido = []

        for produto in self.produtos:
            situacao = produto.situacao()

            if situacao == "Repor" or situacao == "Em falta":
                pedido.append({
                    "codigo": produto.codigo,
                    "nome": produto.nome,
                    "situacao": situacao
            })

        return pedido

    def valor_estoque(self):
        total = 0

        for produto in self.produtos:
            total += produto.quantidade * produto.preco

        return total

    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }