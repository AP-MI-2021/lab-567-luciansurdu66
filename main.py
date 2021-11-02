from Logic.CRUD import adauga_vanzare
from Tests.testAll import test_all
from UserInterface.console import run_menu


def main():
    lst = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 29.71, "gold", lst)
    lst = adauga_vanzare("2", "Metamorfoza", "Nuvela", 23.33, "silver", lst)
    run_menu(lst)


if __name__ == '__main__':
    test_all()
    main()
