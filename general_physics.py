MENDELEEV = {
    "He":4,
    "Ne":20,
    "Ar":40
}


def atom_to_mass(atom:int)-> float:
    """
    Переводит атомную массу в нормальную
    """
    return 1.66*10**(-27)*atom

