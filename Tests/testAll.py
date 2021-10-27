from Tests.testCRUD import test_modifica_vanzare, test_get_by_id, test_sterge_vanzare, test_adauga_vanzare


def test_all():
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_get_by_id()
    test_modifica_vanzare()
