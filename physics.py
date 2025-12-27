from random import *
from math import *
from general_physics import *

class Molecul():
    """
    **`Молекула`**
    - **Назначение:**
        Движущийся объект, имеет массу, способен отражаться, моделирует молекулу газа
    - **Атрибуты**
        - `pos: list[int]` - список координат`(x, y, z)`
        - `V: list[int]` - скорость в разложении на вектора`(Vx, Vy, Vz)`
        - `mass: int` - атомная масса
    - **Методы**
        - `def reverse(i)->float` - отражает скорость координаты i, возвращает импульс
        - `def move(limits: list[int], dt: float) -> int` - функция движения(возвращает переданный импульс)
    """
    def __init__(self, molecul_type: str, avrg_V: int, limits: list[int]):
        self.__pos:list[int] = [randint(0, limits[i]) for i in range(3)]
        abs_V = gauss(avrg_V, avrg_V*2/3)
        angle1 = uniform(0, 2*pi)
        angle2 = uniform(0, 2*pi)
        self.__V:list[int] = [abs_V*cos(angle1)*sin(angle2), 
                                abs_V*sin(angle1), 
                                abs_V*cos(angle1)*cos(angle2)]
        self.__mass:int = MENDELEEV[molecul_type]
    
    @property
    def pos(self):
        return self.__pos
    
    def reverse(self, i: int)->float:
        self.__V[i] = -self.__V[i]
        return abs(atom_to_mass(self.__mass)*2*self.__V[i])
    
    def move(self, limits: list[int], dt: float) -> int:
        imp:float = 0
        for i in range(3):
            self.__pos[i] += dt*self.__V[i]
            if (self.__pos[i] < 0):
                imp += self.reverse(i)
                self.__pos = -self.__pos
            elif (self.__pos > limits):
                imp += self.reverse(i)
                self.__pos = 2*limits[i]-self.__pos
        return imp

    