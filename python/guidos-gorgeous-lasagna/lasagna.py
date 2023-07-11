"""Funções usadas no preparo da linda lasanha do Guido.

Conheça Guido, o criador da linguagem Python:
https://en.wikipedia.org/wiki/Guido_van_Rossum

Este é um módulo docstring, usado para descrever a funcionalidade
de um módulo e suas funções e/ou classes.
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calcule o tempo restante de cozimento.

    :param elapsed_bake_time: int - tempo de cozimento já decorrido.
    :return: int - tempo restante de cozimento (em minutos) derivado de 'EXPECTED_BAKE_TIME'.

    Função que leva os minutos reais que a lasanha ficou no forno como
    uma discussão e retorna quantos minutos a lasanha ainda precisa para assar
    com base em `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# TODO: Defina a função 'preparation_time_in_minutes()' aqui.
# Você também pode considerar usar 'PREPARATION_TIME' aqui, se tiver definido.

def preparation_time_in_minutes(number_of_layers):
    """Calcule o tempo de preparação.

    :param number_of_layers: int - o número de camadas de lasanha feitas.
    :return: int - quantidade de tempo de preparação (em minutos), com base em 2 minutos por camada adicionada.

    Esta função recebe um número inteiro que representa o número de camadas adicionadas ao prato,
    calculando o tempo de preparação usando um tempo de 2 minutos por camada adicionada.
    """

    return number_of_layers * PREPARATION_TIME


# TODO: defina a função 'elapsed_time_in_minutes()' abaixo.
# Lembre-se de adicionar uma docstring (você pode copiar e depois alterar a de bake_time_remaining.)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcule o tempo decorrido.

    :param number_of_layers: int - o número de camadas na lasanha.
    :param elapsed_bake_time: int - tempo de cozimento decorrido.
    :return: int - tempo total decorrido (em minutos) preparando e cozinhando.

    Esta função recebe dois inteiros representando o número de camadas de lasanha e o
    tempo já gasto no cozimento e calcula o total de minutos gastos no cozimento do
    lasanha.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
