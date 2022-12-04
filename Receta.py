#!/usr/bin/python
#-*- coding: utf-8 -*-

class Receta:
    def __init__(self):
        self.Medico = None
        self.Dommed = None
        self.Cedula = None
        self.Inst = None
        self.Esp = None
        self.Fecha = None
        self.Firma = None
        self.Nompac = None
        self.Edadpac = None
        self.Denom = None
        self.Dosis = None
        self.Prec = None
        self.Admin = None
        self.Frec = None
        self.Durac = None
        self.Cant = None
        self.Sello = None

    def Obtener_datos(self):
        """
        
      
        Vacia los atributos en una lista.
      
        Parameters:
      
        Returns:
        list: lista con los atributos separados.
        """
        datos=[]
        datos.append(self.Medico)
        datos.append(self.Dommed)
        datos.append(self.Cedula)
        datos.append(self.Inst)
        datos.append(self.Esp)
        datos.append(self.Fecha)
        datos.append(self.Firma)
        datos.append(self.Nompac)
        datos.append(self.Edadpac)
        datos.append(self.Denom)
        datos.append(self.Dosis)
        datos.append(self.Prec)
        datos.append(self.Admin)
        datos.append(self.Frec)
        datos.append(self.Durac)
        datos.append(self.Cant)
        datos.append(self.Sello)
        return datos

    def Llenardatos(self):
        """
        
      
        Asigna un valor a cada uno de los atributos.
      
        Parameters:
      
        Returns:
      
        """
        self.Medico=input("Ingresa el medico: ")
        self.Dommed=input("Ingresa el domicilio del medico: ")
        self.Cedula=input("Ingresa la cedula: ")
        self.Inst=input("Ingresa el instituto: ")
        self.Esp=input("Ingresa la especialidad: ")
        self.Fecha=input("Ingresa la Fecha: ")
        self.Firma=input("Ingresa la Firma: ")
        self.Nompac=input("Ingresa el nombre del paciente: ")
        self.Edadpac=input("Ingresa la edad del paciente: ")
        self.Denom=input("Ingresa la denominacion generica: ")
        self.Dosis=input("Ingresa la dosis: ")
        self.Prec=input("Ingresa la presentacion: ")
        self.Admin=input("Ingresa la via de administracion: ")
        self.Frec=input("Ingresa la frecuencia: ")
        self.Durac=input("Ingresa el duracion de tratamiento: ")
        self.Cant=input("Ingresa la cantidad: ")
        self.Sello=input("Ingresa el sello: ")

