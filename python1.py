# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:39:19 2023

@author: 57321
"""





    def torres(torre1, torre2):
        x1, y1 = torre1
        x2, y2 = torre2

       
        if x1 == x2 or y1 == y2:
            return True
        else:
            return False


    torre1 = (2, 3)  
    torre2 = (4, 3)  

    if torres(torre1, torre2):
        print("Las torres se amenazan mutuamente.")
    else:
        print("La defecaste no sirves ni para matar una torre")
        
    def alfiles(alfil1, alfil2):
        x1, y1 = alfil1
        x2, y2 = alfil2

      
        if abs(x1 - x2) == abs(y1 - y2):
            return True
        else:
            return False

    # Ejemplo de uso
    alfil1 = (2, 2) 
    alfil2 = (7, 7)  
    if alfiles(alfil1, alfil2):
        print("Los alfiles se amenazan mutuamente.")
    else:
        print("La defecaste no sirves ni para matar un alfil")
        
    def peones_se_amanazan(peon1, peon2):
        x1, y1 = peon1
        x2, y2 = peon2

        # Verificar si los peones están uno casillero diagonalmente el uno del otro
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
            return True
        else:
            return False

    # Ejemplo de uso
    peon1 = (4, 1)  # Coordenadas del primer peón (fila, columna)
    peon2 = (5, 2)  # Coordenadas del segundo peón (fila, columna)

    if peones_se_amanazan(peon1, peon2):
        print("Los peones se amenazan mutuamente.")
    else:
        print("La defecaste no sirves ni para amenazar un peón")
