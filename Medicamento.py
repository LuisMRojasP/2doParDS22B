#!/usr/bin/python
#-*- coding: utf-8 -*-

class Medicamento:
    def __init__(self, med=None):
        self.DatosMed = med

    def EncontrarMed(self, ):
        """
        
      
        Imprime que se ha encontrado el medicamento.
      
        Parameters:
      
        Returns:
      
        """
        print("Medicamento encontrado....")

    def DevolverMed(self):
        """
        
      
        Imprime que se ha devuelto el medicamento.
      
        Parameters:
      
        Returns:
      
        """
        print("Medicamento: "+self.DatosMed[0]+" Devuelto.")

