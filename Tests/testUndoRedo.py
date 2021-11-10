from Logic.CRUD import adauga_vanzare
from Logic.functionalitati import aplicare_discount
from Logic.undo_redo import do_undo, do_redo


def test_undo_redo():

    undo_list = []
    redo_list = []

    # 1
    lst = []
    assert len(lst) == 0

    # 2
    lst = adauga_vanzare(1, "1984", "Roman Politic", 30.0, "gold", lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold']]

    # 3
    lst = adauga_vanzare(2, "Metamorfoza", "Nuvela", 24.0, "silver", lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, "Metamorfoza", "Nuvela", 24.0, "silver"]]

    # 4
    lst = adauga_vanzare(3, "The trial", "Roman", 20, "none", lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, "Metamorfoza", "Nuvela", 24.0, "silver"],
                   [3, "The trial", "Roman", 20, "none"]]

    # 5
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, "Metamorfoza", "Nuvela", 24.0, "silver"]]

    # 6
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold']]

    # 7
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == []

    # 8
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == []

    # 9
    lst = adauga_vanzare(1, "1984", "Roman Politic", 30.0, "gold", lst, undo_list, redo_list)
    lst = adauga_vanzare(2, "Metamorfoza", "Nuvela", 24.0, "silver", lst, undo_list, redo_list)
    lst = adauga_vanzare(3, "The trial", "Roman", 20, "none", lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, "Metamorfoza", "Nuvela", 24.0, "silver"],
                   [3, "The trial", "Roman", 20, "none"]]

    # 10
    lst = do_redo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, "Metamorfoza", "Nuvela", 24.0, "silver"],
                   [3, "The trial", "Roman", 20, "none"]]

    # 11
    lst = do_undo(lst, undo_list, redo_list)
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold']]

    # 12
    lst = do_redo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, "Metamorfoza", "Nuvela", 24.0, "silver"]]

    # 13
    lst = do_redo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, "Metamorfoza", "Nuvela", 24.0, "silver"],
                   [3, "The trial", "Roman", 20, "none"]]

    # 14
    lst = do_undo(lst, undo_list, redo_list)
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold']]

    # 15
    lst = adauga_vanzare(4, "The Communist Manifesto", "Pamphlet", 40.0, "gold", lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [4, "The Communist Manifesto", "Pamphlet", 40.0, "gold"]]

    # 16
    lst = do_redo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [4, "The Communist Manifesto", "Pamphlet", 40.0, "gold"]]

    # 17
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold']]

    # 18
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == []

    # 19
    lst = do_redo(lst, undo_list, redo_list)
    lst = do_redo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [4, "The Communist Manifesto", "Pamphlet", 40.0, "gold"]]

    # 20
    lst = do_redo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [4, "The Communist Manifesto", "Pamphlet", 40.0, "gold"]]


def test_undo_redo_4():
    lst = []
    undo_list = []
    redo_list = []
    lst = adauga_vanzare(1, "1984", "Roman Politic", 30.0, "gold", lst, undo_list, redo_list)
    lst = adauga_vanzare(2, "Metamorfoza", "Nuvela", 24.0, "silver", lst, undo_list, redo_list)
    lst = adauga_vanzare(3, "The trial", "Roman", 20, "none", lst, undo_list, redo_list)
    lst = adauga_vanzare(4, "The Communist Manifesto", "Pamphlet", 40.0, "gold", lst, undo_list, redo_list)
    lst = aplicare_discount(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 27.0, 'none'],
                   [2, 'Metamorfoza', 'Nuvela', 22.8, 'none'],
                   [3, 'The trial', 'Roman', 20, 'none'],
                   [4, 'The Communist Manifesto', 'Pamphlet', 36.0, 'none']]
    lst = do_undo(lst, undo_list, redo_list)
    assert lst == [[1, '1984', 'Roman Politic', 30.0, 'gold'],
                   [2, 'Metamorfoza', 'Nuvela', 24.0, 'silver'],
                   [3, 'The trial', 'Roman', 20, 'none'],
                   [4, 'The Communist Manifesto', 'Pamphlet', 40.0, 'gold']]
