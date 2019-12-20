from django.shortcuts import render
from django.conf import settings
import json
# Create your views here.


def index(request):
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
    return render(request, 'index.html', context=dict_context)
