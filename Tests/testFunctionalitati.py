from Domain.vanzare import get_pret, get_reducere, get_id
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.functionalitati import aplicare_discount, pret_minim_gen, ordonare_dupa_pret


def test_aplicare_discount():
    lst = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 24.95, "gold", lst)
    lst = adauga_vanzare("2", "Metamorfoza", "Nuvela", 29.71, "silver", lst)
    noua_lista = aplicare_discount(lst)
    modificat1 = get_by_id("1", noua_lista)
    modificat2 = get_by_id("2", noua_lista)

    assert get_pret(modificat1) == 22.455
    assert get_reducere(modificat1) == "none"
    assert get_pret(modificat2) == 28.2245
    assert get_reducere(modificat2) == "none"


def test_pret_minim_gen():
    lst = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 24.95, "gold", lst)
    lst = adauga_vanzare("2", "Metamorfoza", "Nuvela", 29.71, "silver", lst)
    lst = adauga_vanzare("3", "3", "Nuvela", 37.82, "none", lst)

    rezultat = pret_minim_gen(lst)

    assert len(rezultat) == 2
    assert rezultat["Nuvela"] == 29.71
    assert rezultat["Roman Politic"] == 24.95


def test_ordonare_dupa_pret():
    lst = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 24.95, "gold", lst)
    lst = adauga_vanzare("2", "Metamorfoza", "Nuvela", 29.71, "silver", lst)
    lst = adauga_vanzare("3", "3", "Nuvela", 37.82, "none", lst)

    rezultat = ordonare_dupa_pret(lst)

    assert get_id(rezultat[0]) == "1"
    assert get_id(rezultat[1]) == "2"
    assert get_id(rezultat[2]) == "3"
