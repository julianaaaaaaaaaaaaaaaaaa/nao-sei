Class Cliente:
    def__init__(self,id, nome, email, fone): 
        self.set_id(id) 
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone) 
    def__str__(self): # type: ignore
        return f"{self.__id}"