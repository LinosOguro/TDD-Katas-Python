import pytest
from string_calculator import add

def test_texto_vazio_retorna_zero():
    assert add('') == 0

def test_um_numero_retorna_o_proprio_numero():
    assert add('1') == 1

def test_soma_numeros_separados_por_virgula():
    assert add('1,2') == 3

def test_aceita_quebra_de_linha_como_separador():
    assert add('1\n2,3') == 6

def test_rejeita_um_numero_negativo():
    with pytest.raises(ValueError) as erro:
        add('-1,2,-3')

    assert "-1" in str(erro.value)
    assert "-3" in str(erro.value)