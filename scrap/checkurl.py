from pip._vendor import requests
import json
import os
from bs4 import BeautifulSoup


dataset = []


"""
soup.find("meta",property="og:title")
soup.find("meta",property="og:description")
soup.find("meta",property="og:image")
soup.find("meta",property="og:url")
"""
F_URL = "url"
F_STATUS = "status_code"
F_HTML = "content"
F_TITLE = "title"
F_IMAGE = "image"
F_DESCRIPTION = "description"
F_COUNT = "count"


def get(url_en_arg):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
    headersdict = {"User-Agent": user_agent}
    req = requests.get(url_en_arg, headers=headersdict)

    req.raise_for_status()
    return req


# def displayJson(jsonFile):
    pass


def writetodict(req, is_verbose=False):
    '''inscrit la réponse de la recherche beautifulSoup dans un dict: puis affecté à la variable global dataset '''
    dict_meta = search_meta(req.text)
    dict_url = {F_STATUS: req.status_code}
    dict_url.update(dict_meta)
    #print("dict update         ***************", dict_url)
    # dataset est defini en global comme une liste
    global dataset
    dataset.append(dict_url)


# def writeToDict(req):
    # créer un dict avec les éléments reçu de req et le renvoie
    pass


# def writeToFile(list):
    # crée un json  à partir d'un dict
    pass


# def seachr_title_by_bs4(text):
    #     soup = BeautifulSoup(text, "lxml")

    #     # ATTENTION CODE TEST DE FIN DE JOURNEE
    #     # d = soup.find_all("h1")
    #     # for h1 in d:
    #     #     print(f"--> h1 : {h1}")
    #     # d = soup.find_all("h1")
    #     # for h2 in d:
    #     #     print(f"--> h2 : {h1}")

    #     # # FIN DE CODE DE FIN DE JOURNEE

    #     # print("***********************************", soup.title.string)
    #     return soup.title.string


def search_meta(text):
    dict_meta = {}
    soup = BeautifulSoup(text, "lxml")
    tit = soup.find("meta", property="og:title")
    if not tit:
        title = soup.title.string
    else:
        title = tit["content"]

    descr = soup.find("meta", property="og:description")
    description = descr["content"] if descr else ""

    ur = soup.find("meta", property="og:url")
    url = ur["content"] if ur else ""

    im = soup.find("meta", property="og:image")
    image = im["content"] if im else ""

    dict_meta = {F_DESCRIPTION: description,
                 F_IMAGE: image, F_URL: url, F_TITLE: title}
    return dict_meta


# def search_title(text):
    # return search_meta(text)
   # return seachr_title_by_bs4(text)

    # DEPRECATED use beautifulSoup instead
    # """ permet de chercher le titre dans une page web """
    # retbuffer = begin = 0
    # end = None
    # begin = text.find("<title>")
    # if begin != -1:
    #     begin += len("<title>")
    #     end = text[begin:].find("</title>")
    #     if end != -1:
    #         end += begin
    #         retbuffer = text[begin:end]
    # print(f"Test search_title : {begin}, {end}, {retbuffer}")
    # return retbuffer


def get_urls(arg, is_verbose=False):

    for arg in listedesurls:
        try:
            req = get(arg)
        except Exception as e:
            print(f"erreurs de requests vers {arg}")
            print(str(e))
            req = None
        if req:
            displayUrl(req, is_verbose)
            writetodict(req, is_verbose)

 # ci-dessous test
    #     texthtml = req.text[:4500]
    #     print("texthtml  ", texthtml)
    #     na = texthtml.find("<title>")
    #     nb = texthtml.find("</title>")
    #     print("********************* na ", na)
    #     print("nb ", nb)
    #     titlesiteurl = texthtml[na+7:nb]
    #     print("**************************        titlesiteurl", titlesiteurl)

    # list.append(writeToDict(req))
    # jsonFile=writeToFile(list)
    # displayJson(jsonFile)


def count_dataset(dataset_input):
    # je compte dataset et crée le fichier json dataset_api
    """fonction qui compte les objets présents dans dataset_api 
        count = number

        dataset_api et dataset = DICT    

    """
    count = len(dataset_input)
    data = {F_COUNT: count, 'dataset': dataset_input}
    return data


def displayUrl(req, is_verbose):
    #print(f"il y a  {len(req.text)} octets and {req.url}")
    print(req.status_code)
    # print(req.headers)
    if is_verbose:
        # print(req.content[:500])
        for key, value in req.headers.items():
            print(f"{key} : {value}")
            # print(req.text)
        print("-"*30)
    return req


if __name__ == '__main__':
    exempleListe = ["matin", "midi", "soir", "minuit", "aube"]
    for item in exempleListe:
        print(item)
        # "http://192.168.1.12:8080/formext/avions/avion
    listedesurls = ["https://www.20minutes.fr/", "https://www.lemonde.fr", "https://www.lemonde.fr", "https://www.youtube.com/?hl=fr&gl=FR",
                    "https://www.ouest-france.fr", "https://www.lemonde.fr", "https://www.python.org/"]

    get_urls(listedesurls, False)

    # attention dataset est global

    print(len(dataset))

    # affiche le nom du fichier .py
    print(__file__)
    # affiche le repertoire absolue pour le système d'exploitation
    print(os.path.abspath(__file__))
    # affiche le répertoire contenant le fichier .py
    print(os.path.dirname(__file__))
    # récupére le nom du fichier dans la configuration du système d'exploitation
    basedir = os.path.dirname(os.path.abspath(__file__))
    print(basedir)
    # création du fichier checkurl.json dans le répertoire scrap
    filename = basedir+"/"+"checkurl.json"

    data_api = count_dataset(dataset)
    # dataset_api ={"count":len(dataset),"dataset":dataset}
    with open(filename, "w+", encoding="utf8") as f:
        json.dump(data_api, f)
        print(f"file {filename} created !")
