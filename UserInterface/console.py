from Domain.vanzare import to_string
from Logic.CRUD import adauga_vanzare, sterge_vanzare, modifica_vanzare
from Logic.functionalitati import aplicare_discount, pret_minim_gen, ordonare_dupa_pret, modifica_gen


def print_menu():
    print("1. Adaugare vanzare.")
    print("2. Stergere vanzare.")
    print("3. Modificare vanzare.")
    print("4. Aplica discount")
    print("5. Modifica genul pentru un titlu dat")
    print("6. Determina pretul minim pentru fiecare gen")
    print("7. Ordoneaza crescator vanzarile dupa pret")
    print("a. Afiseaza toate vanzarile.")
    print("x. Iesire.")


def ui_adauga_vanzare(lst_vanzari):
    id_vanzare = input("Dati id-ul vanzarii: ")
    titlu = input("Dati titlul cartii: ")
    gen = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii: "))
    reducere = input("Dati tipul de reducere client: ")
    return adauga_vanzare(id_vanzare, titlu, gen, pret, reducere, lst_vanzari)


def ui_sterge_vanzare(lst_vanzari):
    try:
        id_vanzare = input("Dati id-ul vanzarii ce trebuie sters: ")
        return sterge_vanzare(id_vanzare, lst_vanzari)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lst_vanzari


def ui_modifica_vanzare(lst_vanzari):
    id_vanzare = input("Dati id-ul vanzarii ce trebuie modificata: ")
    titlu = input("Dati noul titlu al cartii: ")
    gen = input("Dati noul gen al cartii: ")
    pret = float(input("Dati noul pret al cartii: "))
    reducere = input("Dati noul tip de reducere client: ")
    return modifica_vanzare(id_vanzare, titlu, gen, pret, reducere, lst_vanzari)


def ui_aplica_discount(lst_vanzari):
    return aplicare_discount(lst_vanzari)


def show_all(lst_vanzari):
    for vanzare in lst_vanzari:
        print(to_string(vanzare))


def ui_pret_minim_gen(lst_vanzari):
    rezultat = pret_minim_gen(lst_vanzari)
    for gen in rezultat:
        print("Genul {} are pretul minim {}".format(gen, rezultat[gen]))


def ui_ordonare_dupa_pret(lst_vanzari):
    show_all(ordonare_dupa_pret(lst_vanzari))


def ui_modifica_gen(lst_vanzari):
    titlu = input("Dati titlul cartii: ")
    gen = input("Dati noul gen al cartii: ")
    return modifica_gen(titlu, gen, lst_vanzari)


def run_menu(lst_vanzari):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == '1':
            lst_vanzari = ui_adauga_vanzare(lst_vanzari)
        elif optiune == '2':
            lst_vanzari = ui_sterge_vanzare(lst_vanzari)
        elif optiune == '3':
            lst_vanzari = ui_modifica_vanzare(lst_vanzari)
        elif optiune == '4':
            lst_vanzari = ui_aplica_discount(lst_vanzari)
        elif optiune == '5':
            lst_vanzari = ui_modifica_gen(lst_vanzari)
        elif optiune == '6':
            ui_pret_minim_gen(lst_vanzari)
        elif optiune == '7':
            ui_ordonare_dupa_pret(lst_vanzari)
        elif optiune == 'a':
            show_all(lst_vanzari)
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita, reincercati!!")
