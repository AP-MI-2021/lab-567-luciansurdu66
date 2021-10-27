from Domain.vanzare import get_id, get_titlu, get_gen, get_pret, get_reducere
from Logic.CRUD import modifica_vanzare


def aplicare_discount(lst_vanzari: list) -> list:
    """
    Modifica pretul vanzarilor in functie de tipul de reducere aplicat
    :param lst_vanzari: lista de vanzari
    :return: lista cu vanzarile cu preturi modificate
    """
    for vanzare in lst_vanzari:
        id_vanzare = get_id(vanzare)
        titlu = get_titlu(vanzare)
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        reducere = get_reducere(vanzare)
        if reducere == "silver":
            discount = 5 * pret / 100
            lst_vanzari = modifica_vanzare(id_vanzare, titlu, gen, pret - discount, 'none', lst_vanzari)
        elif reducere == "gold":
            discount = 10 * pret / 100
            lst_vanzari = modifica_vanzare(id_vanzare, titlu, gen, pret - discount, 'none', lst_vanzari)
    return lst_vanzari


def modifica_gen(titlu: str, lst_vanzari: list):
    """
    Modifica genul unei carti pentru un titlu dat
    :param titlu: titlul dat
    :param lst_vanzari: lista de vanzari
    :return: lista de vanzari modificata
    """
    pass
