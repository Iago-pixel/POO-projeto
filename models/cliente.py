class Cliente:
    def __init__(self, id, n, e, f):
        self.id = id
        self.nome = n
        self.email = e
        self.fone = f

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def fone(self):
        return self.__fone

    @id.setter
    def id(self, id):
        if id < 1:
            raise ValueError("O valor do id deve ser maior que 0!")
        self.__id = id

    @nome.setter
    def nome(self, n):
        if n == "":
            raise ValueError("O nome é obrigatório!")
        self.__nome = n

    @email.setter
    def email(self, e):
        if e == "":
            raise ValueError("O e-mail é obrigatório!")
        if not "@" in e:
            raise ValueError("Esse e-mail é inválido!")
        self.__email = e

    @fone.setter
    def fone(self, f):
        if f == "":
            raise ValueError("O telefone é obrigatório!")
        self.__fone = f

    def __str__(self):
        return f"id {self.id} - {self.nome} - {self.email} - tel. {self.fone}"

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "fone": self.fone
        }

    @classmethod
    def from_json(cls, dic):
        return cls(**dic)