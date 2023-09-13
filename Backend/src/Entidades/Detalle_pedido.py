class Detalle_pedido :
    
    def __init__(self) :
        pass
        
         
       
        
    @property
    def ID_detalle(self):
        return self._ID_detalle
    
    @property
    def ID_pedido(self):
        return self._ID_pedido
    
    @property
    def ID_producto(self):
        return self._ID_producto
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self,nueva_cantidad):
        self._cantidad = nueva_cantidad
        
    @property
    def subtotal(self):
        return self._subtotal
    
    @subtotal.setter
    def subtotal(self,nuevo_subtotal):
        self._subtotal = nuevo_subtotal
        
    def __str__(self):
        return f"DETALLE DEL PEDIDO : ID: {self.ID_detalle},ID DEL PEDIDO: {self.ID_pedido}, ID DEL PRODUCTO: {self.ID_producto}, Cantidad comprada: {self.cantidad}, Subtotal: {self.subtotal}"