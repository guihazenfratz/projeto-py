class Clientes:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._num = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def telefone1(self):
        return self._num
