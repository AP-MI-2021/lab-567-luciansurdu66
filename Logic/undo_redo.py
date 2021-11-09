def do_undo(lst_vanzari, undo_list, redo_list):
    """

    :param lst_vanzari:
    :param undo_list:
    :param redo_list:
    :return:
    """

    if undo_list:
        redo_list.append(lst_vanzari)
        return undo_list.pop()
    return lst_vanzari


def do_redo(lst_vanzari, undo_list, redo_list):
    """

    :param lst_vanzari:
    :param undo_list:
    :param redo_list:
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(lst_vanzari)
        return top_redo
    return lst_vanzari
