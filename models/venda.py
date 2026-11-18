import datetime as dt


class Venda:
    def __init__(self, id, id_cl):
        self.id = id
        self.data = dt.datetime.now()
        self.carrinho = True
        self.total = 0
        self.id_cliente = id_cl

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def carrinho(self):
        return self.__carrinho

    @property
    def total(self):
        return self.__total

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @data.setter
    def data(self, d):
        self.__data = d

    @carrinho.setter
    def carrinho(self, c):
        self.__carrinho = c

    @total.setter
    def total(self, t):
        if t < 0:
            raise ValueError("O total deve ser positivo!")
        self.__total = t

    @id_cliente.setter
    def id_cliente(self, id_cl):
        if id_cl < 1:
            raise ValueError("O valor do id do cliente deve ser maior que 0!")
        self.__id_cliente = id_cl

    def __str__(self):
        id = self.id
        data = self.data.strftime("%d/%m/%Y")
        carrinho = "Está no carrinho" if self.carrinho else "Não está no carrinho"
        total = f"R$ {self.total:.2f}"
        id_cliente = self.id_cliente
        return f"id {id} - criado em {data} - {carrinho} - total: {total} - id do cliente {id_cliente}"

    def to_json(self):
        return {
            "id": self.id,
            "data": self.data.strftime("%d/%m/%Y"),
            "carrinho": 1 if self.carrinho else 0,
            "total": self.total,
            "id_cliente": self.id_cliente
        }

    @classmethod
    def from_json(cls, dic):
        venda = cls(dic["id"], dic["id_cliente"])
        venda.data = dt.datetime.strptime(dic["data"], "%d/%m/%Y")
        venda.carrinho = bool(dic["carrinho"])
        venda.total = dic["total"]
        return venda