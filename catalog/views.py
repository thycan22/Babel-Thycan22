from django.shortcuts import render
from django.conf import settings
import json
from .models import Dewey, Publication
# Create your views here.

CONTEXT_GLOBAL = {'mediatheque_name': 'Bibliothèque de Saint Pons',
                  "mediatheque_adr": "Villeneuve les Angles",
                  "dev_github": "https://github.com/thycan22/babel-thycan22",
                  "dev_name": "Thierry cantin",
                  "dev_cadre": "formation CDA"}


def publication(request):
    try:
        # record = Dewey.objects.get(number='100')
        record_list = Dewey.objects.all()
        publication_list = Publication.objects.all()
    except:
        record = record_list = publication_list = None

    context_local = {"title": "liste des publications du catalogue",
                     "description": "Publication et leurs références"}

    context_page = {"global": CONTEXT_GLOBAL,
                    "local": context_local,
                    "dewey_object": record,
                    "dewey_object_list": record_list,
                    "publication_object_list": publication_list}
    return render(request, 'catalog/publication.html', context=context_page)


def home(request):
    context_local = {"title": "page d'accueil de Babel",
                     "description": "Bienvenue sur cette page en cours de réalisation"}
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, 'catalog/index.html', context=context_page)


def about(request):
    context_local = {"title": "A propos de Babel",
                     "description": "Vous aurez toute les informations ici."}
    context_page = {"global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, 'catalog/about.html', context=context_page)


def newsroom(request):
    basedir = settings.BASE_DIR
    filename = basedir + '/scrap/checkurl.json'
    try:
        with open(filename, "r", encoding='utf-8') as f:
            dict_check_url = json.load(f)
            print(dict_check_url)
    except Exception as e:
        dict_check_url = {'error': str(e)}
    dict_context = {
        "jumbotron_title": "Bienvenue sur notre projet Babel !",
        "jumbotron_p": "Vous aurez des informations plus tard ....",
        "checkurl": dict_check_url,
    }
    context_local = {"title": "Salle de Presse!!",
                     "description": "Decouvrez une liste de quotidiens internationaux."}
    # pour  ajouter deux dictionaire onedict, anotherdict à un dictionnaire bigdict
    # j'utilise
    # bigdict={**onedict, anotherdict}
    #
    context_page = {**dict_context,
                    "global": CONTEXT_GLOBAL, "local": context_local}
    return render(request, 'catalog/newsroom.html', context=context_page)
