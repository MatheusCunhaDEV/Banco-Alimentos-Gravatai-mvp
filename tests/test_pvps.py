from datetime import date, timedelta
from app import classificar_pvps

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
