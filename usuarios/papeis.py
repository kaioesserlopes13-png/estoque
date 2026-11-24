
# papeis.py — os cargos do sistema e o que cada um pode fazer

PERMISSOES = {
    "solicitante": [
        "ver_produtos",
        "abrir_pedido",
    ],
    "supervisor": [
        "ver_produtos",
        "abrir_pedido",
        "aprovar_pedido",
    ],
    "almoxarifado": [
        "ver_produtos",
        "abrir_pedido",
        "cadastrar_produto",
        "movimentar_estoque",
        "andamento_pedido",
        "cancelar_pedido",
        "aprovar_cadastro",
    ],
    "admin": [
        "ver_produtos",
        "cadastrar_usuario",
        "mudar_papeis",
        "aprovar_cadastro",
    ],
}

# Devolve a lista de papéis existentes
def papeis_validos():
    return list(PERMISSOES.keys())
