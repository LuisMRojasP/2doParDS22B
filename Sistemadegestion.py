#!/usr/bin/python
#-*- coding: utf-8 -*-
from Medicamento import Medicamento
from Receta import Receta
class Sistemadegestion:
    def __init__(self):
        self.Receta = None
        self.DatosMed = None

    def Validar(self):
        """

      
        Funcion para validar los datos de una receta, crea la receta, la llena
        y compara si es correcta o no, para decidir si pasa a surtir o no.
      
        Parameters:
      
        Returns:
      
        """
        rec=Receta()
        rec.Llenardatos()
        self.Receta=rec.Obtener_datos()
        surt=True
        for i in self.Receta:
            if len(i)==0:
                surt=False

        if surt:
            print("Datos correctos.")
            self.DatosMed=self.Receta[10]+","+self.Receta[12]
            self.Surtir()
        else:
            print("Datos incorrectos.")
    def Surtir(self):
        """

      
        Crea un objeto de tipo medicamento al cual se le pasa una lista con 2 
        datos, se llama a encontrar medicamento y devolver medicamento del objeto
        de tipo medicamento.
      
        Parameters:
      
        Returns:
      
        """
        print("Surtiendo medicamento...")
        med=Medicamento(self.DatosMed)
        med.EncontrarMed()
        med.DevolverMed()


