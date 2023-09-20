from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('strtest', 'b')

    with pytest.raises(TypeError):
        encrypt_message(27, 5)

    assert encrypt_message('vitao', 10) == 'oativ'

    assert encrypt_message('vitao', 4) == 'o_ativ'

    assert encrypt_message('vitao', 3) == 'tiv_oa'
