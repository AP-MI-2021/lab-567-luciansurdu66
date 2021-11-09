from Logic.CRUD import adauga_vanzare
from Tests.testAll import test_all
from UserInterface.command_line_console import line_console
from UserInterface.console import run_menu


def main():
    lst = []
    undo_list = []
    redo_list = []
    lst = adauga_vanzare("1", "1984", "Roman Politic", 29.71, "gold", lst, undo_list, redo_list)
    lst = adauga_vanzare("2", "198444", "Roman Politic", 29.71, "gold", lst, undo_list, redo_list)
    lst = adauga_vanzare("3", "Metamorfoza", "Nuvela", 23.33, "silver", lst, undo_list, redo_list)
    menu = str(input("Dati tipul de meniu dorit (basic / command): "))
    if menu == "basic":
        run_menu(lst, undo_list, redo_list)
    elif menu == "command":
        line_console(lst, undo_list, redo_list)


if __name__ == '__main__':
    test_all()
    main()
