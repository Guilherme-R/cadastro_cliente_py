class Endereco:
    def __init__(self, logradouro, cidade, estado, cep):
        self._logradouro = logradouro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep

    @property
    def logradouro(self):
        return self._logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        self._logradouro = logradouro

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep
