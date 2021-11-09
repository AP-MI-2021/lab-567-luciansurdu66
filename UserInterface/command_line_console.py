from Domain.vanzare import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare
from Logic.functionalitati import pret_minim_gen


def print_comenzi():
    print("* Comenzi *")
    print("1. add, id, titlu, gen, pret, tip_reducere (Adauga o vanzare)")
    print("2. delete, id (Sterge o vanzare dupa un id dat)")
    print("3. minimum_price (Afiseaza pretul minim pentru pentru fiecare gen in parte)")
    print("4. show (Afiseaza toate vanzarile existente)")


def show_all(lst_vanzari):
    for vanzare in lst_vanzari:
        print(to_string(vanzare))


def line_console(lst_vanzari, undo_list, redo_list):
    while True:
        print_comenzi()
        toata_comanda = input("Da lista de comenzi. Acestea trebuie despartite prin ;. "
                              "Itemii din cadrul comenzii trebuie despartiti prin virgula"
                              " si nu trebuie sa existe spatiu intre cuvinte ")
        comanda = toata_comanda.split(";")
        for comanda in comanda:
            com = comanda.split(",")
            if com[0] == "add":
                try:
                    lst_vanzari = adauga_vanzare(com[1], com[2], com[3], float(com[4]), com[5], lst_vanzari, undo_list,
                                                 redo_list)
                except ValueError as ve:
                    print("Eroare: ", ve)
            elif com[0] == "delete":
                lst_vanzari = sterge_vanzare(str(com[1]), lst_vanzari, undo_list, redo_list)
            elif com[0] == "minimum_price":
                print(pret_minim_gen(lst_vanzari))
            elif com[0] == "show":
                show_all(lst_vanzari)
            else:
                raise ValueError("Optiune gresita! Verificati lista de comenzi")
