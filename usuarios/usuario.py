
# usuario.py — classe Usuario
# Guarda os dados do usuário e suas permissões.
# A senha é armazenada somente como hash.

import hashlib
import secrets
from usuarios.papeis import PERMISSOES


class Usuario:

    # Construtor
    def __init__(self, matricula, nome, senha, papeis, supervisor=None):
        self.matricula = matricula
        self.nome = nome
        self.papeis = papeis
        self.supervisor = supervisor
        self.situacao = "ativo"

        # Gera um sal aleatório para proteger a senha
        self._sal = secrets.token_hex(8)
        self._senha_hash = self._resumir(senha)

    # Transforma a senha em um resumo (hash)
    def _resumir(self, senha):
        texto = (self._sal + senha).encode("utf-8")
        return hashlib.sha256(texto).hexdigest()

    # Confere se a senha está correta
    def conferir_senha(self, senha):
        return self._resumir(senha) == self._senha_hash

    # Verifica se o usuário possui determinado papel
    def tem_papel(self, papel):
        return papel in self.papeis

    # Verifica se o usuário possui determinada permissão
    def pode(self, permissao):

        # Usuário inativo não possui permissões
        if self.situacao != "ativo":
            return False

        # Percorre todos os papéis do usuário
        for papel in self.papeis:

            # Verifica as permissões de cada papel
            if permissao in PERMISSOES[papel]:
                return True

        return False

    # Junta todas as permissões sem repetir
    def permissoes(self):
        lista = []

        for papel in self.papeis:
            for permissao in PERMISSOES[papel]:

                if permissao not in lista:
                    lista.append(permissao)

        return lista

    # Troca a senha do usuário
    def trocar_senha(self, atual, nova):

        # Confere a senha atual
        if not self.conferir_senha(atual):
            return False

        # Atualiza o resumo da senha
        self._senha_hash = self._resumir(nova)

        return True

    # Devolve os dados do usuário em formato de dicionário
    def para_dicionario(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "papeis": self.papeis,
            "permissoes": self.permissoes(),
            "supervisor": self.supervisor,
            "situacao": self.situacao
        }
