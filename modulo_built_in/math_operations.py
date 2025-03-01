# modulo de operações matematicas

def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Não é permitido divisao por zero.")