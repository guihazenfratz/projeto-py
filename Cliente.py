class Clientes:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone
