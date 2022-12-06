import os
import random

class weapons:
    def __init__(self, category, name, firerate, ammunitiontype, ammunitioncount):
        self.category = category
        self.name = name
        self.firerate = firerate
        self.ammunitiontype = ammunitiontype
        self.ammunitioncount = ammunitioncount

pistol_list = ["Beretta m9","Glock 19"]

pl = random.choice(pistol_list)
ac = random.randint(1,20)

has_magazine = False
h_m = random.randint(0,1)
if h_m == 0:
    has_magazine = False
if h_m == 1:
    has_magazine = True


firearm = weapons("Firearm",pl,"Semi-Automatic","9mm",ac)

print(firearm.category,">",firearm.name,">",firearm.ammunitiontype,">",firearm.ammunitioncount)

        
# Weapon // Inventory system
# WORK IN PROGRESS
