from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext as _
import xlrd
from xlwt import Workbook, Formula
from .utils import get_century

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Prénom"),)
    last_name = models.CharField(max_length=30, verbose_name=_("Nom"),)
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(
        null=True, blank=True, editable=False, verbose_name=_("Siècle"),)
    date_birth = models.DateField(
        null=True, blank=True, verbose_name=_("Date de naissance"),)
    place_birth = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Lieu de naissance"),)

    date_died = models.DateField(
        null=True, blank=True, verbose_name=_("Date de décès"),)
    place_died = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Lieu de décès"),)
    content = models.TextField(
        null=True, blank=True, verbose_name=_("Contenu"),)
    image_url = models.URLField(
        null=True, blank=True, verbose_name=_("URL d'image"),)
    image_file = models.ImageField(
        null=True, blank=True, verbose_name=_("Chemin du fichier image"),)

    class Meta:
        ordering = ["last_name"]
        verbose_name = _("Auteur")

    def __str__(self):
        if self.first_name:
            return f"{self.last_name}, {self.first_name} "
        else:
            return self.last_name

    def clean(self):
        """
        update of century from <date_birth> using catalog.utils.get_century function
        update name in <first_name space last_name> or <last_name>
        """

        if self.date_birth:
            # century
            self.century_birth = get_century(self.date_birth.year)
            return self.century_birth
        if self.first_name:
            return f"{self.last_name}, {self.first_name} "
        else:
            self.name = self.last_name


class Dewey(models.Model):

    ''' attention liste ordonnée'''

    BG_COLOR_CHOICES = [
        ("000", "#000000", "#FFFFFF", "black"),  # Black 000
        ("100", "#8B4513", "#FFFFFF", "maroon"),  # Maroon 100
        ("200", "#FF0000", "#FFFFFF", "red"),  # Red 200
        ("300", "#FF4500", "#000000", "orange"),  # Orange 300
        ("400", "#FFFF00", "#000000", "yellow"),  # Yellow 400
        ("500", "#32CD32", "#000000", "green"),  # Green 500
        ("600", "#1E90FF", "#000000", "blue"),  # Blue 600
        ("700", "#8B008B", "#FFFFFF", "purple"),  # Purple 700
        ("800", "#A9A9A9", "#FFFFFF", "grey"),  # Grey 800
        ("900", "#FFFFFF", "#000000", "white"),  # White 900

    ]

    TEXT_COLOR_CHOICES = [
        ("#000000", "black"),
        ("#FFFFFF", "white"),
    ]

    name = models.CharField(max_length=61, verbose_name=_("Catégorie"),)
    number = models.CharField(
        max_length=12, default='000', verbose_name=_("Numéro Dewey"),)
    bg_color = models.CharField(max_length=7,
                                null=True, blank=True, editable=False)
    text_color = models.CharField(
        max_length=7, null=True, blank=True, editable=False, default='#000000')

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} - {self.name}"

    def xls_reader(self):
        ''' permet de lire un fichier xls du répertoire /scrap/ grace à l'import xlrd 

        '''
        path = "scrap/La_Dewey_simplifiee.xls"
        number = []
        # ouverture du classeur
        classeur = xlrd.open_workbook(path)

        # Récupération du nom de toutes les feuilles sous forme de liste
        nom_des_feuilles = classeur.sheet_names()

        # Récupération de la première feuille
        feuille = classeur.sheet_by_name(nom_des_feuilles[0])
        for i in range(0, 109):
            # for j in range(0, 1):
                # print(u"Lecture des cellules:")
                # print("A1: {}".format(feuille.cell_value(i, j)))
            if feuille.cell_value(i, 1):
                item = Dewey(number=feuille.cell_value(i, 1),
                             name=feuille.cell_value(i, 2))
                item.save()
                print("Number: {}".format(feuille.cell_value(i, 1)))
                # elif !(feuille.cell_value(i, 1)) and feuille.cell_value(i, 2):
                # self.name = feuille.cell_value(i, 2)

    def clean(self):
        # self.xls_reader()
        str_number = str(int(self.number))
        if len(str_number) < 3:
            str_number = str(int(self.number))
            if len(str_number) < 2:
                str_number = '00' + str_number
            else:
                str_number = '0' + str_number
            self.number = str_number

    # def set_dewey_color_publication(self):
    #     return format_html(
    #         '<span style="background-color: {}; color: {};">{}</span>',
    #         self.bg_color,
    #         self.text_color,
    #         self.name,
    #     )

    def set_dewey_color_publication(self):
        if self.number:
            try:
                i = int(self.number[:1])
                return format_html(
                    '<div style="background-color: {}; color: {};min-width: 150px;">{}</div>',
                    self.BG_COLOR_CHOICES[i][1],
                    self.BG_COLOR_CHOICES[i][2],
                    self.name,
                )
            except:
                return "Wrong Format"

    # def set_dewey_color_publication(self):
    #     for i in range(0, len(self.BG_COLOR_CHOICES)):
    #         if self.number[:1] == str(i):
    #             self.bg_color = self.BG_COLOR_CHOICES[i][0]
    #             self.text_color = self.BG_COLOR_CHOICES[i][1]
    #     return format_html(
    #         '<span style="background-color: {}; color: {};">{}</span>',
    #         self.bg_color,
    #         self.text_color,
    #         self.name,
    #     )

    # def set_dewey_color_publication(self):
    #     if self.number[:1] == '0':
    #         self.bg_color = self.BG_COLOR_CHOICES[0][0]
    #         self.text_color = self.TEXT_COLOR_CHOICES[1][0]
    #     elif self.number[:1] == '1':
    #         self.bg_color = self.BG_COLOR_CHOICES[1][0]
    #     elif self.number[:1] == '2':
    #         self.bg_color = self.BG_COLOR_CHOICES[2][0]
    #     elif self.number[:1] == '3':
    #         self.bg_color = self.BG_COLOR_CHOICES[3][0]
    #     elif self.number[:1] == '4':
    #         self.bg_color = self.BG_COLOR_CHOICES[4][0]
    #     elif self.number[:1] == '5':
    #         self.bg_color = self.BG_COLOR_CHOICES[5][0]
    #     elif self.number[:1] == '6':
    #         self.bg_color = self.BG_COLOR_CHOICES[6][0]
    #     elif self.number[:1] == '7':
    #         self.bg_color = self.BG_COLOR_CHOICES[7][0]
    #         self.text_color = self.TEXT_COLOR_CHOICES[1][0]
    #     elif self.number[:1] == '8':
    #         self.bg_color = self.BG_COLOR_CHOICES[8][0]
    #         self.text_color = self.TEXT_COLOR_CHOICES[1][0]
    #     elif self.number[:1] == '9':
    #         self.bg_color = self.BG_COLOR_CHOICES[9][0]
    #         self.text_color = self.TEXT_COLOR_CHOICES[0][0]
    #     return format_html(
    #         '<span style="background-color: {}; color: {};">{}</span>',
    #         self.bg_color,
    #         self.text_color,
    #         self.name,
    #     )


class Publication(models.Model):

    TYPEPUBLICATION_CHOICES = [
        ("B", "Books"),
        ("M", "Music"),
        ("F", "Film"),
        ("_", "Autre")
    ]
    isbn = models.CharField(max_length=13, null=True,
                            blank=True, verbose_name=_("ISBN"),)
    name = models.CharField(max_length=61, verbose_name=_("Nom de l'oeuvre"),)
    type_publication = models.CharField(
        max_length=1, choices=TYPEPUBLICATION_CHOICES, default='B', verbose_name=_("type de parution"),)
    genre = models.CharField(max_length=35, null=True, blank=True)
    author = models.ForeignKey(
        Author, models.PROTECT, verbose_name=_("Autheur"),)
    reference = models.CharField(
        max_length=61, null=True, blank=True, editable=False, verbose_name=_("Référence interne"),)
    dewey_number = models.ForeignKey(
        Dewey, models.PROTECT, verbose_name=_("Numero Dewey"),)
    date_publication = models.DateField(
        null=True, blank=True, verbose_name=_("Date de publication"),)
    nb_tracks_pages = models.IntegerField(
        null=True, blank=True, verbose_name=_("Pages/Pistes"),)
    label_editor = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Label/Editeur"),)
    content = models.TextField(
        null=True, blank=True, verbose_name=_("Contenu"),)
    image_url = models.URLField(
        null=True, blank=True, verbose_name=_("URL de l'image"),)
    image_file = models.ImageField(
        null=True, blank=True, verbose_name=_("Chemin du fichier"),)

    # permet d'ordonner l'affichage

    class Meta:
        ordering = ["reference"]

    # permet d'afficher une valeur dans la page home de publication à la place de 'object'

    def __str__(self):
        return f"{self.reference} {self.name} {self.author}"

    def clean(self):
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = ""
