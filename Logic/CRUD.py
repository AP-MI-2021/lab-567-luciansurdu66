from Domain.vanzare import get_id, creeaza_vanzare


def adauga_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere, lst_vanzari):
    """
    Adauga o vanzare in lista
    :param id_vanzare: sting
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere: string
    :param lst_vanzari: lista de vanzari
    :return: o noua lista formata din lst_vanzari si noua vanzare adaugata
    """
    vanzare = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere)
    return lst_vanzari + [vanzare]


def get_by_id(id_vanzare, lst_vanzari):
    """
    ia cartea din librarie cu id-ul dat
    :param id_vanzare: string
    :param lst_vanzari: lista de vanzari
    :return: cartea cu id-ul dat sau None, daca nu exista cartea cu id-ul dat
    """
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            return vanzare
    return None


def sterge_vanzare(id_vanzare, lst_vanzari):
    """
    Sterge o vanzare din lista
    :param id_vanzare: id-ul vanzarii pe care vrem sa o stergem
    :param lst_vanzari: lista de vanzari
    :return: noua lista ce nu contina vanzarea cu id-ul id_vanzare
    """
    return [vanzare for vanzare in lst_vanzari if get_id(vanzare) != id_vanzare]


def modifica_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere, lst_vanzari):
    """
    Modifica o vanzare din lista dupa id
    :param id_vanzare: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere: string
    :param lst_vanzari: lista de vanzari
    :return: lista modificata
    """
    new_list = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_noua = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere)
            new_list.append(vanzare_noua)
        else:
            new_list.append(vanzare)
    return new_list
