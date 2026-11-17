import html
from datetime import datetime

def sanitizar_texto(texto: str) -> str:
    """Previne Cross-Site Scripting (XSS) limpando espaços e escapando tags HTML."""
    if not texto or not texto.strip():
        raise ValueError("O campo de texto obrigatório não pode estar vazio.")
    return html.escape(texto.strip())

def validar_baixa_estoque(saldo_atual: float, quantidade_retirada: float) -> float:
    """Garante integridade de saldo na baixa de saída (RF03)."""
    if quantidade_retirada <= 0:
        raise ValueError("A quantidade retirada deve ser maior que zero.")
    if quantidade_retirada > saldo_atual:
        raise ValueError("Saldo insuficiente no lote para esta retirada.")
    return round(saldo_atual - quantidade_retirada, 2)
