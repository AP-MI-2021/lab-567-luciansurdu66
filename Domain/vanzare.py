def creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere):
    """
    creeaza un dictionar ce reprezinta o vanzare
    :param id_vanzare: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere: string
    :return: un dictionar ce reprezinta o vanzare
    """
    return [id_vanzare, titlu_carte, gen_carte, pret, tip_reducere]
    """
    return {
        "id": id_vanzare,
        "titlu": titlu_carte,
        "gen": gen_carte,
        "pret": pret,
        "reducere": tip_reducere
    }
    """


def get_id(vanzare):
    """
    da id-ul unei vanzari
    :param vanzare: vanzarea
    :return: id-ul vanzarii - strig
    """
    return vanzare[0]
    # return vanzare["id"]


def get_titlu(vanzare):
    """
    da titlul unei carti din lista
    :param vanzare: vanzarea
    :return: titlul cartii - string
    """
    return vanzare[1]
    # return vanzare["titlu"]


def get_gen(vanzare):
    """
    da genul unei carti
    :param vanzare: vanzarea
    :return: genul cartii
    """
    return vanzare[2]
    # return vanzare["gen"]


def get_pret(vanzare):
    """
    da pretul unei carti
    :param vanzare: vanzarea
    :return: pretul cartii
    """
    return vanzare[3]
    # return vanzare["pret"]


def get_reducere(vanzare):
    """
    da reducerea tip client
    :param vanzare: vanzarea
    :return: reducerea tip client
    """
    return vanzare[4]
    # return vanzare["reducere"]


def to_string(vanzare):
    return "id: {}, titlu: {}, gen: {}, pret: {}, reducere: {}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )
