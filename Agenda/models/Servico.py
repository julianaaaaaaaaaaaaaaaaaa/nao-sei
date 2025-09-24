class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f}"

    
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_valor(self, valor): self.__valor = float(valor)

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "valor": self.__valor
        }

    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])
