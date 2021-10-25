from Domain.vanzare import get_pret, get_reducere
from Logic.CRUD import adauga_vanzare, get_by_id
from Logic.functionalitati import aplicare_discount


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


