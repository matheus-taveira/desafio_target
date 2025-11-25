import json

# 1. Dados Iniciais de Estoque [cite: 50, 51, 52]
ESTOQUE_DADOS_JSON = """
{
"estoque":
[
{ "codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150 },
{ "codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75 },
{ "codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200 },
{ "codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320 },
{ "codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90 }
]
}
"""

# Inicializa o estado do estoque (variável global simulando o banco de dados)
def inicializar_estoque(dados_json: str) -> dict:
    dados = json.loads(dados_json)
    # Mapeia por codigoProduto para acesso rápido
    return {item['codigoProduto']: item for item in dados['estoque']}

ESTOQUE_ATUAL = inicializar_estoque(ESTOQUE_DADOS_JSON)
MOVIMENTACOES_REGISTRO = []
ULTIMO_ID_MOV = 0

def lancar_movimentacao(codigo_produto: int, tipo_movimentacao: str, quantidade: int, descricao_mov: str) -> str:
    """
    Registra uma movimentação no estoque.
    tipo_movimentacao: 'ENTRADA' ou 'SAIDA'
    """
    global ULTIMO_ID_MOV
    
    if codigo_produto not in ESTOQUE_ATUAL:
        return f"Erro: Produto {codigo_produto} não encontrado."

    produto = ESTOQUE_ATUAL[codigo_produto]
    
    # Define o ajuste (+ para entrada, - para saída)
    ajuste_estoque = 0
    tipo = tipo_movimentacao.upper()

    if tipo == 'ENTRADA':
        ajuste_estoque = quantidade
    elif tipo == 'SAIDA':
        if produto['estoque'] < quantidade:
            return f"Erro na Saída: Saldo insuficiente de {produto['descricaoProduto']}. Estoque atual: {produto['estoque']}."
        ajuste_estoque = -quantidade
    else:
        return "Erro: Tipo de movimentação inválida."

    # Atualiza o estoque
    produto['estoque'] += ajuste_estoque

    # Registra a movimentação [cite: 47, 48, 49]
    ULTIMO_ID_MOV += 1
    movimentacao = {
        "id": ULTIMO_ID_MOV,
        "codigoProduto": codigo_produto,
        "tipo": tipo,
        "quantidade": quantidade,
        "descricaoMovimentacao": descricao_mov,
        "saldoFinal": produto['estoque']
    }
    MOVIMENTACOES_REGISTRO.append(movimentacao)
    
    return f"Mov. ID {ULTIMO_ID_MOV} concluída. Saldo final de **{produto['descricaoProduto']}** ({codigo_produto}): **{produto['estoque']}** un."

if __name__ == "__main__":
    print("--- Lançamentos de Movimentação de Estoque ---")
    print(lancar_movimentacao(101, 'ENTRADA', 50, 'Compra Lote 2025')) # 150 + 50 = 200
    print(lancar_movimentacao(103, 'SAIDA', 20, 'Venda para Cliente Alpha')) # 200 - 20 = 180
    print(lancar_movimentacao(102, 'ENTRADA', 10, 'Ajuste de Inventário')) # 75 + 10 = 85
    print(lancar_movimentacao(105, 'SAIDA', 100, 'Venda para Cliente Beta')) # 90 - 100 = Erro

    print("\n--- Saldo Final Atualizado ---")
    for codigo, prod in ESTOQUE_ATUAL.items():
        print(f"Cód: {codigo} - **{prod['descricaoProduto']}**: {prod['estoque']}")