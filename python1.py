# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:39:19 2023

@author: 57321
"""

def peones_se_amanazan(peon1, peon2):
    x1, y1 = peon1
    x2, y2 = peon2

    
    if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
        return True
    else:
        return False


peon1 = (4, 3)  
peon2 = (5, 3)  

if peones_se_amanazan(peon1, peon2):
    print("Los peones se amenazan mutuamente.")
else:
    print("La defecaste no sirves ni para amenazar un peón:(")



