class Cliente:
    def __init__(self, id, nome, email, fone):
        self._id = id
        self._nome = nome
        self._email = email
        self._fone = fone

    def __str__(self):
        return f"ID: {self._id} | Nome: {self._nome} | Email: {self._email} | Fone: {self._fone}"

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_fone(self):
        return self._fone

    def set_nome(self, nome):
        self._nome = nome

    def set_email(self, email):
        self._email = email

    def set_fone(self, fone):
        self._fone = fone
