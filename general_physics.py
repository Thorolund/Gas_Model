from math import *

MENDELEEV = {
    "He":4,
    "Ne":20,
    "Ar":40
}
BOLZMAN_K =  1.4 * 10**(-23)

def atom_to_mass(atom:int)-> float:
    """
    Переводит атомную массу в нормальную
    """
    return 1.66*10**(-27)*atom

def vector_coord(abs_size, angle1, angle2):
        return [abs_size*cos(angle1)*sin(angle2), 
                abs_size*sin(angle1), 
                abs_size*cos(angle1)*cos(angle2)]
