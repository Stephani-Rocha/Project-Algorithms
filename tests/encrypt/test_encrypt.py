from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("trybe", -1) == "ebyrt"
    assert encrypt_message("trybe", 3) == "yrt_eb"
    assert encrypt_message("trybe", 4) == "e_byrt"
    assert encrypt_message("trybe", 5) == "ebyrt"

    with pytest.raises(TypeError):
        encrypt_message(1, 2)

    with pytest.raises(TypeError):
        encrypt_message("trybe", "trybe")
