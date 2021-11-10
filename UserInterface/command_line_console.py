from Domain.vanzare import to_string, creeaza_vanzare, get_id
from Logic.CRUD import get_by_id
from Logic.functionalitati import pret_minim_gen


def print_comenzi():
    print("* Comenzi *")
    print("1. add, id, titlu, gen, pret, tip_reducere (Adauga o vanzare)")
    print("2. delete, id (Sterge o vanzare dupa un id dat)")
    print("3. minimum_price (Afiseaza pretul minim pentru pentru fiecare gen in parte)")
    print("4. show (Afiseaza toate vanzarile existente)")


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


def show_all(lst_vanzari):
    for vanzare in lst_vanzari:
        print(to_string(vanzare))


def line_console(lst_vanzari, undo_list, redo_list):
    while True:
        show_all(lst_vanzari)
        print_comenzi()
        toata_comanda = input("Da lista de comenzi. Acestea trebuie despartite prin ;. "
                              "Itemii din cadrul comenzii trebuie despartiti prin virgula"
                              " si nu trebuie sa existe spatiu intre cuvinte: ")
        comanda = toata_comanda.split(";")
        for comanda in comanda:
            com = comanda.split(",")
            if com[0] == "add":
                try:
                    lst_vanzari = adauga_vanzare(int(com[1]), com[2], com[3], float(com[4]), com[5], lst_vanzari,
                                                 undo_list, redo_list)
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif com[0] == "delete":
                lst_vanzari = sterge_vanzare(int(com[1]), lst_vanzari, undo_list, redo_list)
            elif com[0] == "minimum_price":
                print(pret_minim_gen(lst_vanzari))
            elif com[0] == "show":
                show_all(lst_vanzari)
            else:
                raise ValueError("Optiune gresita! Verificati lista de comenzi")
