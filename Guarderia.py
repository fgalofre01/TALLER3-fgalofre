from Huron import Huron
from Boa_Constrictor import Boa_Constrictor


class Guarderia():
    
    def __init__(self):
        self.boas = [Boa_Constrictor("Boa1",25.5,10,"Colombia",0.16), 
                    Boa_Constrictor("Boa2",20.5,8,"Colombia",0.16)
                    ]
        self.hurones = [Huron("Huron1",25.5,10,"Colombia",0.16), 
                        Huron("Huron2",20.5,8,"Colombia",0.16)]
    
    def alimentar_boa(self,boa):
            if boa is None:
                return "Esta Boa no existe!"  # Si la boa recibida es None
            try:
               boa.comer_raton()# Intentamos alimentar la boa
               return "Exito"  # Si no hay excepción, el mensaje de éxito
            except ValueError as e:
               return f"La boa esta llena, {e}"  # Retornamos el mensaje de la excepción ("Demasiados Ratones!")
