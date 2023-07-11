def exchange_money(budget, exchange_rate):
    """

    :param budget: float - quantidade de dinheiro que você planeja trocar.
    :param exchange_rate: float - valor unitário da moeda estrangeira.
    :return: float - valor de troca da moeda estrangeira que você pode receber.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - quantidade de dinheiro que você possui.
    :param exchanging_value: float - valor do seu dinheiro que você deseja trocar agora.
    :return: float - valor restante da sua moeda inicial após a troca.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - o valor de uma nota.
    :param number_of_bills: int - quantidade de contas que você recebeu.
    :return: int - valor total das notas que você tem agora.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - a quantidade de dinheiro que você planeja trocar.
    :param denomination: int - o valor de uma única nota.
    :return: int - número de notas depois de trocar todo o seu dinheiro.
    """

    return int(budget) // denomination


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - a quantidade de dinheiro que você planeja trocar.
    :param denomination: int - o valor de uma única nota.
    :return: float - o valor restante que não pode ser trocado dada a denominação atual.
    """

    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - a quantidade de dinheiro que você planeja trocar.
    :param exchange_rate: float - o valor unitário da moeda estrangeira.
    :param spread: int - porcentagem que é tomada como taxa de câmbio.
    :param denomination: int - o valor de uma única nota.
    :return: int - valor máximo que você pode obter.
    """

    taxa_cambio = (exchange_rate / 100) * spread
    exchange_value = exchange_money(budget, exchange_rate + taxa_cambio)
    number_of_bills = get_number_of_bills(exchange_value, denomination)
    value_of_bills = get_value_of_bills(denomination, number_of_bills)
    return value_of_bills
