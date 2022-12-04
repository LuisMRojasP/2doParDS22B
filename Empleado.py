#!/usr/bin/python
#-*- coding: utf-8 -*-
from Sistemadegestion import Sistemadegestion

class Empleado:
    def __init__(self):
        self.Nombre = None
        self.Edad = None

    def Entrarsist(self, ):
        """

      
        Funcion para crear un objeto sistema.
      
        Parameters:
      
        Returns:
      
        """
        self.Nombre="Luis"
        self.Edad="22"
        print(self.Nombre + " ha entrado al sistema")
        sist=Sistemadegestion()
        sist.Validar()
