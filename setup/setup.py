"""
Setup v0.1
Programme qui affiche le setup de python
Changelog:
-dec 19: initialisation
"""

#  premier programme - setup v0.1

import sys
import os
import datetime


def printseparator():
    """ fonction qui affiche une ligne de séparation"""
    print("-" * 50)


printseparator()
a = 'bonjour monde !'
print(a)  # j'affiche a#

printseparator()

print(sys.executable)
print(sys.platform)
print(sys.path)

print(sys.version_info)
v = sys.version_info
print(type(v))
print(dir(v))

print(f"python version {v.major}.{v.minor}.{v.micro}")
print("python version {}.{}.{}".format(v.major, v.minor, v.micro))

printseparator()

print("python version %s.%s.%s" %
      (v.major, v.minor, v.micro))  # Version 2.7, déprécié

print("Environnement PythonPath : " + os.getenv('PYTHONPATH', 'vide'))
print(datetime)
print(datetime.__file__)

printseparator()

dt = datetime.datetime.now()
print(f"Date et heure :{dt} - Année {dt.year}")

printseparator()
help(printseparator)
