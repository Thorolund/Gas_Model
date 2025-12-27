from random import *
from math import *
from general_physics import *

class Molecule():
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
        self.__V:list[int] = vector_coord(abs_V, angle1, angle2)
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
                self.__pos[i] = -self.__pos[i]
            elif (self.__pos[i] > limits[i]):
                imp += self.reverse(i)
                self.__pos[i] = 2*limits[i]-self.__pos[i]
        return imp

class Room():
    """
    **`Комната`**
    - **Назначение:**
    Комната, внутри которой находятся молекулы газа. Отражает модекулы
    - **Атрибуты:**
        - `size:list[int]` - размер комнаты (x, y, z)
        - `molecules:list[Molecule]` - все молекулы в комнате
        - `measure:dict[str:Any]` - величины, полезные для рассчетов
        - `dt:float` - отрезок времени, через который мы смотрим изменения
    - **Методы**
        - `def tick() -> dict[str:Any]` - проход по всем клеткам, возврат посчитанных величин
    """
    def __init__(self, N:int, T:float, size:list[int], element:str):
        avrg_V = (3*BOLZMAN_K*T/atom_to_mass(MENDELEEV[element]))
        self.molecules = [Molecule(element, avrg_V, size) for i in range(N)]
        self.size = size
        self.measure:dict[str:float|int] = {"P":0}
        self.__dt = 0.00001
    @property
    def dt(self):
        return self.__dt
    @dt.setter
    def dt(self, new_dt):
        self.__dt = max(0, new_dt)
        
    def tick(self):

        F = 0
        for molecule in self.molecules:
            F += molecule.move(self.size, self.__dt)/self.dt
        self.measure["P"] = F/(2*(self.size[0]*self.size[1] + self.size[1]*self.size[2] +
                                  self.size[0]*self.size[2]))
        return self.measure
    
    