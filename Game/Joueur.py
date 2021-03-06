"""
    Potentiellement documenter le module ici mais ne pas trop le faire parce que c'est pour les faibles
"""
import Plateau0
from visual import *
from math import *

class Joueur:

    def __call__(self):
        print("foo")

    def __init__(self, pion, name):
        self.name = name
        self.pion = pion
        self.pions = []
        self.cubes = []
        if (pion == 1):
            self.init_pions(1, 2)
        else:
            self.init_pions(2, 1)
        pass

    def set_cubes(self, cubes):
        self.cubes = cubes

    def get_associate_pion(self, ref):
        for i in range(len(self.cubes)):
            if ref.pos == self.cubes[i].pos:
                ref.visible = False
                self.cubes.pop(i)
                return self.pions.pop(i)
            pass
        pass
        return -1

    def init_pions(self, maj, min):
        for i in range(13):
            self.pions.append(maj)
        pass
        for i in range(5):
            self.pions.append(min)
        pass

    def is_pion_available(self, pion):
        return pion < len(self.pions)

    def __str__(self):
        sb = self.name + ": ["
        for i in range(len(self.pions)):
            sb = sb + str(i) + ": " + str(self.pions[i]) + " "
        pass
        sb += "]"
        return sb
