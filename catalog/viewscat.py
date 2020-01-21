from django.views.generic import TemplateView, ListView, DetailView
from django.utils.translation import gettext as _
from .models import Publication, Dewey
from .views import CONTEXT_GLOBAL


class MixinContextPage():
    title = _("Mon Titre")
    description = _("Ma description")

    def get_mycontext(self):

        context_local = {
            "title": self.title,
            "description": self.description,
        }

        context_page = {
            "global": CONTEXT_GLOBAL,
            "local": context_local,
        }
        return context_page

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context_page = self.get_mycontext()
        # retour de deux dictionnaires : context page et context global
        return {**context, **context_page}


class PublicationByDewey(MixinContextPage, ListView):
    template_name = "catalog/publication.html"
    context_object_name = "publication_object_list"
    # queryset = Publication.objects.all()
    # ajout du MixinContextPage pour hériter d'un context_local et context global
    # Ajout du support de traduction
    title = _("Liste de publications par Dewey N°: {}")
    description = _("Vous trouverez les publications classées par Dewey")

    def get_queryset(self):
         # argument deweynumber provenant de la structure de l'url
        deweynumber = self.kwargs["deweynumber"]

        # requete sur les pulications avec le classement Dewey spécifié dans l'URL
        queryset = Publication.objects.filter(dewey_number__number=deweynumber)

        # ou requete avec l'objet Dewey
        self.currentdewey = Dewey.objects.get(number=deweynumber)
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in the publisher
        # requete pour avoir la liste du classement de Dewey
        context['dewey_object_list'] = Dewey.objects.all()

        # ajout de l'élément dewey actif
        context['dewey_active'] = self.currentdewey

        # appel de la fonction get_mycontext() de MixinContextPage
        # traduction avec le dewey number de l'URL
        # self.title = _("Liste de publications par Dewey N°:{}").format(
        # self.kwargs["deweynumber"])
        # ou avec le display name de l'objet currentdewey récupéré dans get_queryset()
        self.title = self.title.format(self.currentdewey)

        context_page = self.get_mycontext()
        # retour de deux dictionnaires : context page et context global
        return {**context, **context_page}


class PublicationDetail(MixinContextPage, DetailView):
    template_name = "catalog/publication-detail.html"
    model = Publication
    # ajout du MixinContextPage pour hériter d'un context_local et context global
    # Ajout du support de traduction
    title = _("Ma Publication:  ")


"""
class PublicationDetail(TemplateView):
    template_name = "catalog/publication.html"

"""
