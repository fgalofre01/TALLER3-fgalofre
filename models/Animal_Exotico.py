from models.Animal import Animal

class Animal_exotico(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuesto ):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuesto = impuesto
      
    @property
    def pais_origen(self)->str:
        return self._pais_origen
    
    @pais_origen.setter
    def pais_origen(self,pais_origen: str) -> None :
        self._pais_origen = pais_origen
        
    @property
    def impuesto(self)-> float:
        return self._impuesto
    
    @impuesto.setter
    def impuesto(self,impuesto: float) -> None:
        self._impuesto = impuesto
    
    def hacer_sonido(self) -> str :
        return "Estos animales hacen un sonido caracteristico"
        
    def calcular_flete(self)-> float:
        return self.impuesto * self._peso
    
    
    
