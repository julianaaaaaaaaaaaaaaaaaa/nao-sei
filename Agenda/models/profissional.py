class Profissional:
    def __init__(self, id, nome, email, fone, senha, especialidade):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha
        self.__especialidade = especialidade

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha
    def get_especialidade(self): return self.__especialidade

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def set_senha(self, senha): self.__senha = senha
    def set_especialidade(self, especialidade): self.__especialidade = especialidade

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__email} - ({self.__fone}) - ({self.__senha}) - ({self.__especialidade}))"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "senha": self.__senha,
            "especialidade": self.__especialidade
        }

    @staticmethod
    def from_json(d):
        return Profissional(
            d["id"], d["nome"], d["email"], d["fone"], d["senha"], d["especialidade"]
        )
