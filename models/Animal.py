from abc import ABC,abstractmethod
from models.IAnimal import IAnimal

class Animal(IAnimal,ABC):
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad 
        self._kilos_comidos = 1.5
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre: str) -> None:
        self._nombre = nombre
    
    @property
    def peso(self) -> float:
        return self._peso
    
    @peso.setter
    def peso(self,peso : float) -> None:
        self._peso = peso
        
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self,edad: int) -> None:
        self._edad = edad
    
    def comer(self,kilos) -> float:
        self._kilos_comidos += kilos
        
    def obtener_kilos_comidos(self) -> float :
        return self._kilos_comidos
    
    @abstractmethod    
    def hacer_sonido(self) -> str :
        pass
    
    def obtener_nombre(self) -> str:
        return self.nombre
    
    def obtener_peso(self) -> float :
        return self.peso
    
    def obtener_edad(self) -> int :
        return self.edad