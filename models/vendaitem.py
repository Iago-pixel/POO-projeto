class VendaItem:
    def __init__(self, id, q, p, id_ven, id_pr):
        self.id = id
        self.qtd = q
        self.preco = p
        self.id_venda = id_ven
        self.id_produto = id_pr

    @property
    def id(self):
        return self.__id

    @property
    def qtd(self):
        return self.__qtd

    @property
    def preco(self):
        return self.__preco

    @property
    def id_venda(self):
        return self.__id_venda

    @property
    def id_produto(self):
        return self.__id_produto

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @qtd.setter
    def qtd(self, q):
        if q < 0:
            raise ValueError("A quantidade em estoque deve ser positiva!")
        self.__qtd = q

    @preco.setter
    def preco(self, p):
        if p < 0:
            raise ValueError("O preço deve ser positivo!")
        self.__preco = p

    @id_venda.setter
    def id_venda(self, id_ven):
        if id_ven < 1:
            raise ValueError("O valor do id da venda deve ser maior que 0!")
        self.__id_venda = id_ven

    @id_produto.setter
    def id_produto(self, id_pr):
        if id_pr < 1:
            raise ValueError("O valor do id do produto deve ser maior que 0!")
        self.__id_produto = id_pr

    def __str__(self):
        return f"id {self.id} - quantidade: {self.qtd} - R$ {self.preco:.2f} - id_venda {self.id_venda} - id_produto {self.id_produto}"

    def to_json(self):
        return {
            "id": self.id,
            "qtd": self.qtd,
            "preco": self.preco,
            "id_venda": self.id_venda,
            "id_produto": self.id_produto
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)