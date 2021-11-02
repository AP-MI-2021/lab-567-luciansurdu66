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


def modifica_gen(title, gen, lst_vanzari):
    """
    Modifica genul unei carti pentru un titlu dat
    :param title: Titlul cartii
    :param gen: Genul nou
    :param lst_vanzari: Lista de vanzari
    :return: Lista modificata
    """
    for vanzare in lst_vanzari:
        id_vanzare = get_id(vanzare)
        titlu = get_titlu(vanzare)
        pret = get_pret(vanzare)
        reducere = get_reducere(vanzare)
        if get_titlu(vanzare) == title:
            lst_vanzari = modifica_vanzare(id_vanzare, titlu, gen, pret, reducere, lst_vanzari)
    return lst_vanzari


def pret_minim_gen(lst_vanzari):
    """
    Determina pretul minim pentru fiecare gen
    :param lst_vanzari: lista de vanzari
    :return: Fiecare gen cu pretul minim
    """
    rezultat = {}
    for vanzare in lst_vanzari:
        pret = get_pret(vanzare)
        gen = get_gen(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat


def ordonare_dupa_pret(lst_vanzari):
    """
    Ordoneaza crescator vanzarile dupa pret
    :param lst_vanzari: lista de vanzari
    :return: lista de vanzari ordonata crescator dupa pret
    """
    return sorted(lst_vanzari, key=lambda vanzare: get_pret(vanzare))
