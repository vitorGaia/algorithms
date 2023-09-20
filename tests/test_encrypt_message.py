import sys
import os
import pytest
from challenges.challenge_encrypt_message import encrypt_message
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_if_key_not_int():
    '''
    Testa se a função lança um erro ao passar um key que não é tipo int
    '''
    with pytest.raises(TypeError):
        encrypt_message('strtest', 'b')


def test_if_message_not_str():
    '''
    Testa se a função lança um erro ao passar um message que não é tipo str
    '''
    with pytest.raises(TypeError):
        encrypt_message(27, 5)


def test_if_key_bigger_then_message_length():
    '''
    Testa se a função lança um erro ao passar um key maior que largura do
    message retorna message invertida
    '''
    assert encrypt_message('vitao', 10) == 'oativ'


def test_key_pair():
    '''
    Testa o retorno caso key seja par
    '''
    assert encrypt_message('vitao', 4) == 'o_ativ'


def test_key_odd():
    '''
    Testa o retorno caso key seja ímpar
    '''
    assert encrypt_message('vitao', 3) == 'tiv_oa'
