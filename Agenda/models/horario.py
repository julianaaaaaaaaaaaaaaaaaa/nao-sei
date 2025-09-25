from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(False)
        self.set_id_cliente(0)
        self.set_id_servico(0)

    def __str__(self):   
         return f"{self.__id}- self.__data.strftime('%d/%m/%Y %H:%M')}
