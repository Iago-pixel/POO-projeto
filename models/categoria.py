class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

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

    def __str__(self):
        return f"id {self.id} - {self.descricao}"

    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)