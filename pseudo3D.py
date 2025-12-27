import arcade
from physics import *

def vector_to_screen(vector:list[float], h_delta=0, w_delta=0):
    new_coords = [vector[0], vector[1]]
    new_z = vector[2]*0.46
    new_coords[0]-=new_z*cos(pi/6)+w_delta
    new_coords[1]-=new_z*sin(pi/6)+h_delta
    return new_coords

def draw_molecule(molecule:Molecule, h_delta=0, w_delta=0):
    arcade.draw_circle_filled(*vector_to_screen(molecule.pos, h_delta, w_delta), 5, arcade.color.RED)