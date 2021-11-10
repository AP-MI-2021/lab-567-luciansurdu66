from Domain.vanzare import get_id, creeaza_vanzare


def adauga_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere, lst_vanzari, undo_list, redo_list):
    """
    Adauga o vanzare in lista
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param id_vanzare: sting
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere: string
    :param lst_vanzari: lista de vanzari
    :return: o noua lista formata din lst_vanzari si noua vanzare adaugata
    """
    if get_by_id(id_vanzare, lst_vanzari) is not None:
        raise ValueError("Exista deja o vanzare cu acest id!")
    else:
        vanzare = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere)
        undo_list.append(lst_vanzari)
        redo_list.clear()
        return lst_vanzari + [vanzare]
    return lst_vanzari


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


def sterge_vanzare(id_vanzare, lst_vanzari, undo_list, redo_list):
    """
    Sterge o vanzare din lista
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param id_vanzare: id-ul vanzarii pe care vrem sa o stergem
    :param lst_vanzari: lista de vanzari
    :return: noua lista ce nu contina vanzarea cu id-ul id_vanzare
    """
    if get_by_id(id_vanzare, lst_vanzari) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return [vanzare for vanzare in lst_vanzari if get_id(vanzare) != id_vanzare]


def modifica_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere, lst_vanzari, undo_list, redo_list):
    """
    Modifica o vanzare din lista dupa id
    :param redo_list: lista pentru redo
    :param undo_list: lista pentru undo
    :param id_vanzare: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere: string
    :param lst_vanzari: lista de vanzari
    :return: lista modificata
    """
    if get_by_id(id_vanzare, lst_vanzari) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    new_list = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_noua = creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere)
            new_list.append(vanzare_noua)
        else:
            new_list.append(vanzare)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_list
