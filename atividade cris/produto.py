class Produto:
    def __init__(self, nome = None,preco = 0.0, quantidade = 0,categoria = None, peso = 0, codigo = None):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria
        self.peso = peso
        self.codigo = codigo

        def situacao(self):
            if self.quantidade == 0:
                return "em falta"
            elif self.quantidade < 8:
                return "repor"
            else:
                return "ok"
            def listar_produtos(sef):
                return{
                    "nome": self.nome,
                    "preco": self.preco,
                    "quantidade": self.quantidade,
                    "categoria": self.categoria,
                    "peso": self.peso,
                    "codigo": self.codigo,
                    }
