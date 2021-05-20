class Usuario:
    def __init__(self, nome, senha, email, endereco):
        self._nome = nome
        self._senha = senha
        self._email = email
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco


    #
    # @property
    # def cpf(self):
    #     return self._cpf
    #
    # @cpf.setter
    # def cpf(self, cpf):
    #     self._cpf = cpf
