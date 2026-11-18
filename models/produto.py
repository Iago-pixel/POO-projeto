class Produto:
    def __init__(self, id, d, p, e, id_cat):
        self.id = id
        self.descricao = d
        self.preco = p
        self.estoque = e
        self.id_categoria = id_cat

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque

    @property
    def id_categoria(self):
        return self.__id_categoria

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @descricao.setter
    def descricao(self, d):
        if d == "":
            raise ValueError("A descrição é obrigatória!")
        self.__descricao = d

    @preco.setter
    def preco(self, p):
        if p < 0:
            raise ValueError("O preço deve ser positivo!")
        self.__preco = p

    @estoque.setter
    def estoque(self, e):
        if e < 0:
            raise ValueError("O estoque deve ser positivo!")
        self.__estoque = e

    @id_categoria.setter
    def id_categoria(self, id_cat):
        if id_cat < 1:
            raise ValueError("O valor do id_categoria deve ser maior que 0!")
        self.__id_categoria = id_cat

    def __str__(self):
        return f"id {self.id} - {self.descricao} - R$ {self.preco:.2f} - N° no estoque: {self.estoque} - id da categoria {self.id_categoria}"

    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque,
            "id_categoria": self.id_categoria
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)