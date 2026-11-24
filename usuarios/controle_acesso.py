
# controle_acesso.py
# A classe ControleAcesso guarda os usuários e cuida do login.

import secrets
from usuarios.papeis import papeis_validos

# Mensagem padrão para credenciais inválidas
CREDENCIAL_INVALIDA = "Matrícula ou senha inválida."


class ControleAcesso:

    # Construtor
    def __init__(self):
        self.usuarios = []
        self.sessoes = {}

    # Busca um usuário pela matrícula
    def buscar(self, matricula):
        for u in self.usuarios:
            if u.matricula == matricula:
                return u
        return None

    # Cadastra um usuário novo
    def cadastrar(self, usuario):
        achado = self.buscar(usuario.matricula)

        if achado is not None:
            return False

        self.usuarios.append(usuario)
        return True

    # Realiza o login e gera um token
    def entrar(self, matricula, senha):
        usuario = self.buscar(matricula)

        if usuario is None:
            return None

        if not usuario.conferir_senha(senha):
            return None

        if usuario.situacao != "ativo":
            return None

        token = secrets.token_hex(16)

        self.sessoes[token] = matricula

        return token

    # Identifica o usuário através do token
    def usuario_logado(self, token):
        matricula = self.sessoes.get(token)

        if matricula is None:
            return None

        return self.buscar(matricula)

    # Encerra a sessão do usuário
    def sair(self, token):
        if token not in self.sessoes:
            return False

        del self.sessoes[token]

        return True

    # Altera os papéis de um usuário
    def mudar_papeis(self, quem, matricula, papeis):

        # Verifica a permissão de quem está realizando a alteração
        if not quem.pode("mudar_papeis"):
            return "Você não tem permissão para mudar papéis."

        # Verifica se o usuário existe
        usuario = self.buscar(matricula)

        if usuario is None:
            return "Usuário não encontrado."

        # Verifica se a lista de papéis está vazia
        if not papeis:
            return "Escolha pelo menos um papel."

        # Verifica se todos os papéis são válidos
        for papel in papeis:
            if papel not in papeis_validos():
                return "Papel inválido: " + papel

        # Atualiza os papéis do usuário
        usuario.papeis = papeis.copy()

        return None
