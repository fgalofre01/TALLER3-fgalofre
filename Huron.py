from Animal_Exotico import Animal_exotico

class Huron(Animal_exotico):
    
   def __init__(self, nombre, peso, edad, pais_origen, impuesto):
        super().__init__(nombre, peso, edad, pais_origen, impuesto)
       
   def hacer_sonido(self)->str:
        return "¡Eek Eek!"
    
   
    
    