import json
from .vendaitem import VendaItem


class VendaItemDAO:
    def __init__(self):
        self.__arquivo = "venda_item.json"
        self.__objetos = []

    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.id).id
        obj.id = id + 1
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.id == id:
                return obj
        return None

    def atualizar(self, novo_venda_item):
        self.__abrir()
        for i, venda_item_atual in enumerate(self.__objetos):
            if novo_venda_item.id == venda_item_atual.id:
                self.__objetos[i] = novo_venda_item
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, venda_item_atual in enumerate(self.__objetos):
            if venda_item_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            venda_items_json = json.load(arquivo)
            for obj in venda_items_json:
                vi = VendaItem.from_json(obj)
                self.__objetos.append(vi)

    def __salvar(self):
        venda_items_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(venda_items_json, arquivo, indent = 2)