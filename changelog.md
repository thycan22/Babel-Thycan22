#suivi des modifications Babel
(suivi à destination de l'équipe)

changelog v0.0.1

17/12:
-install Python 3.8 et Git
-Algorythme chaine de caractère: fonction input,  "Full name" vers "<firstname><middle><lastname>"
-Dictionnaire est une liste de key/value déclaré via {}
-import de modules dont sys, os : importation des fonctions et objets associés version python --version-- 3.8.0 majeur, mineur , macro
-fonction print avec print(f"Ceci affiche à l'écran une :{variable}") ou "{}.format(variable)
-fonction split- séparation chaînes de caractères par un séparateur par défaut " " (l'espace)
-type() permet de connaître la classe : isinstance(a,classe) exemple: Objets de classe int, str,boolean,dict,list,def().
-Opérateurs  assigné =, <,>,+,*
-Regex -expressions régulières


18/12
-Test unnitaire dont assertEqual
Try, Except, exception
Git, Github
Fonctions dates dont calcul avec deux dates
-MVC Design pattern sur traitement d'une chaîne et de son affichage avec un controlleur
-Tester la classe d'un objet isinstance(a,class)
-readme.md format markdown

19/12
-opérateur Callable () --call--(self)    --add--(self)
-Version majeur,mineur,mIcro V0.0.1
-amélioration de l'installation de python afin d'installer des modules externes: REQUEST(Http POST,GET...) BEAUTIFULSOAP(scraping d'une page Http) DJANGO(serveur web et ses bibliothèques)
-découverte du code source python:
-virtualenv-->permet d'utiliser une configuration d'environnement propre à chaque projet et cela sur n'importe quel machine. on peut spécifier quel python on veut travailler et quel package on télécharge

méthode 1: venv/requirements.txt(requests=3.0.1...)
par exemple pour Babel-thycan22/venv/python....../site-packages
puis pip install request

Methode 2: pipenv
