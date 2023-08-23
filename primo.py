def primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def test_primos():
    assert primo(2)
    assert primo(3)
    assert primo(5)
    assert primo(7)
    assert primo(11)
    assert primo(13)
