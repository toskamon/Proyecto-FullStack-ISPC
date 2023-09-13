from Enums.Estado import Estado
class Pedido:
    def __init__(self):
        
        self._formas_de_pago = [] 
        
    @property
    def ID_pedido(self):
        return self._ID_pedido
         
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self,fecha_nueva):
        self._fecha = fecha_nueva
      
    #de id_usuario solo establezco el getter y no el setter ya que es una clave foranea y no voy a necesitar setearlo 
    @property
    def ID_usuario(self):
        return self._ID_usuario
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,total_nuevo):
        self._total = total_nuevo
        
  
        
    def get_estado(self):
        return self._estado

    
    def set_estado(self, estado):
        if isinstance(estado, Estado):
            self._estado = estado
        else:
            raise ValueError("El valor de estado debe ser un objeto de la clase Estado")
        
    
    def __str__(self):
        return f"PEDIDO(ID:{self.ID_pedido}, Fecha: {self.fecha}, ID_usuario: {self.ID_usuario}, Total: {self.total}, Estado:{self.get_estado().value})"
    
    
