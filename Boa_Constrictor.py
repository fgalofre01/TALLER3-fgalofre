from Animal_Exotico import Animal_exotico

class Boa_Constrictor(Animal_exotico):
    
    def __init__(self, nombre, peso, edad, pais_origen, impuesto):
        super().__init__(nombre, peso, edad, pais_origen, impuesto)
        self._ratones_comidos = 0
    
    def hacer_sonido(self)-> str:
        return "¡Tsss!"
    
    def get_ratones_comidos(self) -> int:
        return self._ratones_comidos
    
    def comer_raton(self):
        if self._ratones_comidos >= 20:
           # Lanza excepción si ha comido 10 ratones
           raise ValueError("Demasiado ratones!")
           # Incrementa el contador si no ha alcanzado el límite
        self._ratones_comidos += 1  
        return self._ratones_comidos
                    
    
