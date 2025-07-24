from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, data_nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento  # formato esperado: "dd/mm/yyyy"

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nNascimento: {self.data_nascimento}"

    
    def get_id(self):
        return self.id

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_telefone(self):
        return self.telefone

    def set_data_nascimento(self, data):
        self.data_nascimento = data

    def get_data_nascimento(self):
        return self.data_nascimento
