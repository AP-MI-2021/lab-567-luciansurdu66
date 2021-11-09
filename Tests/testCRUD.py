from Domain.vanzare import get_id, get_titlu, get_gen, get_pret, get_reducere
from Logic.CRUD import adauga_vanzare, sterge_vanzare, get_by_id, modifica_vanzare


def test_adauga_vanzare():
    vanzare = adauga_vanzare("1", "1984", "Roman Politic", 24.95, "none", [], [], [])

    assert len(vanzare) == 1
    assert get_id(vanzare[0]) == "1"
    assert get_titlu(vanzare[0]) == "1984"
    assert get_gen(vanzare[0]) == "Roman Politic"
    assert get_pret(vanzare[0]) == 24.95
    assert get_reducere(vanzare[0]) == "none"


def test_sterge_vanzare():
    lst = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 24.95, "none", lst, [], [])
    lst = adauga_vanzare("2", "Metamorfoza", "Nuvela", 29.71, "silver", lst, [], [])
    lst = sterge_vanzare("2", lst, [], [])

    assert get_by_id("1", lst) is not None
    assert get_by_id("2", lst) is None


def test_get_by_id():
    lst = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 24.95, "none", lst, [], [])
    lst = adauga_vanzare("2", "Metamorfoza", "Nuvela", 29.71, "silver", lst, [], [])

    assert get_by_id("2", lst) is not None
    assert get_by_id("5", lst) is None


def test_modifica_vanzare():
    lst = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 24.95, "none", lst, [], [])
    lst = adauga_vanzare("2", "Metamorfoza", "Nuvela", 29.71, "silver", lst, [], [])
    lst = modifica_vanzare("1", "1984", "Roman Politic", 24.99, "none", lst, [], [])
    vanzare_modificata = get_by_id("1", lst)

    assert get_pret(vanzare_modificata) == 24.99
