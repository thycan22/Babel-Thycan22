# suivi des modifications Babel
(suivi à destination de l'équipe)

changelog v0.0.1

# semaine 2 Django Babel

## 07/01/2020

### généralités
- rappel web serveur cycle thread d'une reqête http.
(serveur static(CDN:c content delivery network ), bdd)
- Django, les url et les données static pour être accessibles doivent-être autorisés d'accès grâce à urls.py
on accède à nos données static sur serveur distants nginx par exemple ou apache par url.
  * content-type : static

### Django
- doc: voir la doc django officiel pour la syntaxe
- bdd/ORM définitions des modèles dans models.py. Création de class=nom de table pour créer un modèle avec des (propriétés et type)=nom des champs
- models.py : en plus des modèle(table) et propriétés(champs) on peut mettre de l'intelligence. 'def __str__' pour l'affichage en clair de la donnée , ordering des affichages... 
- admin.py : déclarer les modèles, modifier l'affichage de base de Django exemple pour Publication: PublicationAdmin 
- Architecture:
  * respect impératif de la nomenclature code et entreprise.
  * compréhension du besoin client.
  * définir l'objet de l'application.
  * definition de deux personna sur les quatres.
- Objet:
  * Construction de l'interface backoffice pour la gestion du catalogue d'une médiathèque.
### retour utilisateurs et clients
#### partie A
#####  Aide à la saisie
- temps 0: menu déroulant 
        - date
- temps 1:
        - annuler 
        - rassembler les données et les ordonnées en affichage
        - tenir compte de l'objet livre, musique, vidéo
        - champs obligatoire (étoile rouge)
- temps 2:
        - image file
- temps 3:
        - saisie auto-complétion sur auteur, publications
#### partie B
- images
- amélioration

## 08/01/2020
- Django Babel : 
  * Modèle BDD
    * changement d'un modéle de l'application catalog (Dewey Author Publication) puis makemigrations et migrate

  * Modèle fonctions métiers:
      * Modéle DEWEY : ajout des couleurs Dewey dans table Dewey.
      * Modèle Author : ajout de la donnée calculée century.

  * Modéle Admin
      * Formulaire = Définition d'un mode
      * Formulaire redéfinition de l'affichage: regrouper en section les zones d'affichage
        pour être en accord avec le métier et l'objet de la table auteur et publication.
        list_display, fieldsets, read_only, radio_fields.

- Architecture/Gestion de fonctionnalités de l'application.
  * réflexion sur les choix de fonctionnalités de "saisie formulaire" à prendre :
      * parfois les devs spécifiques s'évitent par une formation/accompagnement de l'utilisateur final.
      * retour de l'expérience métier, permet de corriger ou orienter le dev.
      * priorisation de développement/ordonnancement de dev



- Algorythme : recherche du siècle avec une date en entrée yyyy/mm/dd

## 09/01/2020

- Django Babel :
  * Modele admin: formulaire : affichage: ajout de fonctinnalité 'affichage automatique de la couleur Dewey suite à l'insertion d'une publication'
  * ajout des de la possibilité de traductions des noms des champs: <(verbose_name="xxxx"),>

# Semaine 1  Python Algorythmes

## 17/12:
- install Python 3.8 et Git
- Algorythme chaine de caractère: fonction input,  "Full name" vers "<firstname><middle><lastname>"
- Dictionnaire est une liste de key/value déclaré via {}
- import de modules dont sys, os : importation des fonctions et objets associés version python   *version  * 3.8.0 majeur, mineur , macro
- fonction print avec print(f"Ceci affiche à l'écran une :{variable}") ou "{}.format(variable)
- fonction split- séparation chaînes de caractères par un séparateur par défaut " " (l'espace)
- type() permet de connaître la classe : isinstance(a,classe) exemple: Objets de classe int, str,boolean,dict,list,def().
- Opérateurs  assigné =, <,>,+,*
- Regex -expressions régulières


## 18/12
- Test unitaire dont assertEqual
Try, Except, exception
Git, Github
Fonctions dates dont calcul avec deux dates
- MVC Design pattern sur traitement d'une chaîne et de son affichage avec un controleur
- Tester la classe d'un objet isinstance(a,class)
- readme.md format markdown

## 19/12
- opérateur Callable ()   *call  *(self)      *add  *(self)
- Version majeur,mineur,micro V0.0.1
- amélioration de l'installation de python afin d'installer des modules externes: REQUEST(Http POST,GET...) BEAUTIFULSOAP(scraping d'une page Http) DJANGO(serveur web et ses bibliothèques)

- découverte du code source python. opensource dont datetime.py \python38\lib\..

- package requests: - Http get url ....
                   - header requête Http, ajout de la valeur clé:User-agent et valeur:'Mozilla/N02.....' que l'on trouve dans le - - navigateur dans l'inspecteur/network/

- black save sans erreurs de LINT, aide à la réindentation, et à la cosmétique , lisibilité du code   *->FORMAT

- virtualenv  *>permet d'utiliser une configuration d'environnement propre à chaque projet et cela sur n'importe quel machine. on peut spécifier quel python on veut travailler et quel package on télécharge
          * environnement python "propre", précise = version downloadable de python.org
          * répertoire de stockage de votre env se trouve dans /user/.virtualenv/....
          * pipfile->version humaine
          * pipfile.lock->version machine -sécurité d'intégrité des versions de python  *hash  *
        (requirements.txt/pip freeze) requirements.txt


##### méthode 1: venv/requirements.txt(requests=3.0.1...)
- par exemple pour Babel-thycan22/venv/python....../site-packages
puis pip install request

##### Methode 2: pipenv


- installation de l'environnement en pipenv black 

- package Http installation
- premier algo lecture de url et affichage de la réponse en console
        Main()
            - liste de 3 urls
            - itération sur la liste avec: get_url(listurl,bool)  ->none
            <attention au retour par gestion des erreurs>

        get()  .status_code 
                .headers (soit auth, clé auth, user psw etc..)
                .text ->Html

        searchtitle(text)                   fonction find
        
 package beautifulsoup4   de PYpi.org 
        -> outil de scraping ->récupère contenus du web
        -> format html en entrée
                ->analyse le DOM Doc Obj Model(DOM=arborescence des balises html)
        ->''soup.title''
                .find_all('<h1'>)
debuguer 
        -script execution sous win10, accés autorisé
                enlever le warning w291 (mettre un \n enfin de ) chez Flake8(->Lint aide à la syntaxe avant d'attendre la compilation)
## 20/12
# DJango (2h) 
 - create superuser admin->authentification CRUD model(bdd)
 - create user 
 - settings.py (config django)
 - view home affiche contenu json checkurl.py, def home()->url
 - template home.html(index.html) avec bootstrap
        
- checkurl, soup meta donnée
- count dans list dataset

- Django cheet sheet
