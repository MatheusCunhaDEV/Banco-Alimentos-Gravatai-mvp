from datetime import date, timedelta
from app import app, classificar_pvps
from validacoes import sanitizar_texto, validar_baixa_estoque
import pytest

# --- TESTES UNITÁRIOS (Regras PVPS e Validações) ---

def test_alerta_urgente_ate_7_dias():
    data_curta = (date.today() + timedelta(days=4)).strftime("%Y-%m-%d")
    resultado = classificar_pvps(data_curta)
    assert resultado["nivel"] == "URGENTE"
    assert resultado["icone"] == "⚠"

def test_alerta_atencao_entre_8_e_15_dias():
    data_media = (date.today() + timedelta(days=12)).strftime("%Y-%m-%d")
    resultado = classificar_pvps(data_media)
    assert resultado["nivel"] == "ATENÇÃO"

def test_alerta_normal_acima_de_15_dias():
    data_longa = (date.today() + timedelta(days=40)).strftime("%Y-%m-%d")
    resultado = classificar_pvps(data_longa)
    assert resultado["nivel"] == "NORMAL"

def test_sanitizacao_xss():
    entrada_maliciosa = "  <script>alert('xss')</script>Arroz  "
    saida_segura = sanitizar_texto(entrada_maliciosa)
    assert "<script>" not in saida_segura
    assert "&lt;script&gt;" in saida_segura

def test_baixa_estoque_valida_e_insuficiente():
    assert validar_baixa_estoque(50.0, 15.0) == 35.0
    with pytest.raises(ValueError):
        validar_baixa_estoque(10.0, 20.0)

# --- TESTE DE INTEGRAÇÃO (Rota Web Flask) ---

def test_integracao_rota_principal():
    cliente = app.test_client()
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert b"Banco de Alimentos" in resposta.data
