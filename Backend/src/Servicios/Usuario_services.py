from Entidades.Usuario import *
from Repositorio.Usuario_repositorio import *
from Validaciones.validacion_campos import *


def crear_usuario(num):
 try:
     
     usuario1= Usuario()
     nombre= input("por favor,ingrese su nombre ")
     validacion_campo(nombre) or validacion_caracter(nombre,"NOMBRE")
     usuario1.nombre= nombre
     
     apellido=input("ingrese su apellido ")
     validacion_campo(apellido) or validacion_caracter(apellido,"APELLIDO")
     usuario1.apellido= apellido
     
     email=input("ingrese su email ")
     validacion_campo(email)
     usuario1.email= email
     
     dni = int(input("ingrese su numero de documento sin puntos "))
     validacion_numero(dni,"DNI")
     usuario1.dni= dni
     
     domicilio=input("ingrese su domicilio ")
     validacion_campo(domicilio)
     usuario1.domicilio = domicilio
     
     if num == 1:
      usuario1.set_rol(Rol.CLIENTE)
     else:
      usuario1.set_rol(Rol.ADMIN)
     rol = usuario1.get_rol().value
     id= crear_user(nombre,apellido,email,dni,domicilio,rol)
     usuario1.ID_usuario=id
     return usuario1
     
             
 except ValueError as error:
  print("Error:", error)
  
  
  