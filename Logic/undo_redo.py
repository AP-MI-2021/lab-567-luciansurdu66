def do_undo(lst_vanzari, undo_list, redo_list):
    """
    Face un undo
    :param lst_vanzari: lista curenta
    :param undo_list: lista pentru undo
    :param redo_list: lista pentru redo
    :return: lista curenta in cazul in care nu se poate face undo
    """

    if undo_list:
        redo_list.append(lst_vanzari)
        return undo_list.pop()
    return lst_vanzari


def do_redo(lst_vanzari, undo_list, redo_list):
    """
    Face un redo
    :param lst_vanzari: lista curenta
    :param undo_list: lista pentru undo
    :param redo_list: lista pentru redo
    :return: lista curenta in cazul in care nu se poate face redo
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(lst_vanzari)
        return top_redo
    return lst_vanzari
