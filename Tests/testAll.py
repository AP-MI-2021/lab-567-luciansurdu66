from Tests.testCRUD import test_modifica_vanzare, test_get_by_id, test_sterge_vanzare, test_adauga_vanzare
from Tests.testFunctionalitati import test_pret_minim_gen, test_aplicare_discount, test_ordonare_dupa_pret
from Tests.testUndoRedo import test_undo_redo, test_undo_redo_4


def test_all():
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_get_by_id()
    test_modifica_vanzare()
    test_aplicare_discount()
    test_pret_minim_gen()
    test_ordonare_dupa_pret()
    test_undo_redo()
    test_undo_redo_4()
