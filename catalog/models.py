from django.db import models
from django.utils.html import format_html
from .utils import get_century

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(null=True, blank=True, editable=False)
    date_birth = models.DateField(null=True, blank=True)
    place_birth = models.CharField(max_length=50, null=True, blank=True)

    date_died = models.DateField(null=True, blank=True)
    place_died = models.CharField(max_length=30, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        if self.first_name:
            return f"{self.last_name}, {self.first_name} "
        else:
            return self.last_name

    def clean(self):
        if self.date_birth:
            # century
            self.century_birth = get_century(self.date_birth.year)
        return self.century_birth


class Dewey(models.Model):

    BG_COLOR_CHOICES = [
        ("#000000", "black"),  # Black 000
        ("#8B4513", "maroon"),  # Maroon 100
        ("#FF0000", "red"),  # Red 200
        ("#FF4500", "orange"),  # Orange 300
        ("#FFFF00", "yellow"),  # Yellow 400
        ("#32CD32", "green"),  # Green 500
        ("#1E90FF", "blue"),  # Blue 600
        ("#8B008B", "purple"),  # Purple 700
        ("#A9A9A9", "grey"),  # Grey 800
        ("#FFFFFF", "white"),  # White 900

    ]

    TEXT_COLOR_CHOICES = [
        ("#000000", "black"),
        ("#FFFFFF", "white"),
    ]

    name = models.CharField(max_length=61)
    number = models.CharField(max_length=3, default='000')
    bg_color = models.CharField(max_length=7,
                                null=True, blank=True, editable=False)
    text_color = models.CharField(
        max_length=7, null=True, blank=True, editable=False, default='-')

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} - {self.name}"

    # def colored_number(self):
    #     return format_html(
    #         '<span style="background-color: {}; color: {};">{}</span>',
    #         self.bg_color,
    #         self.text_color,
    #         self.name,
    #     )

    def set_dewey_color_publication(self):
        if self.number[:1] == '0':
            self.bg_color = self.BG_COLOR_CHOICES[0][0]
            self.text_color = self.TEXT_COLOR_CHOICES[1][0]
        elif self.number[:1] == '1':
            self.bg_color = self.BG_COLOR_CHOICES[1][0]
        elif self.number[:1] == '2':
            self.bg_color = self.BG_COLOR_CHOICES[2][0]
        elif self.number[:1] == '3':
            self.bg_color = self.BG_COLOR_CHOICES[3][0]
        elif self.number[:1] == '4':
            self.bg_color = self.BG_COLOR_CHOICES[4][0]
        elif self.number[:1] == '5':
            self.bg_color = self.BG_COLOR_CHOICES[5][0]
        elif self.number[:1] == '6':
            self.bg_color = self.BG_COLOR_CHOICES[6][0]
        elif self.number[:1] == '7':
            self.bg_color = self.BG_COLOR_CHOICES[7][0]
            self.text_color = self.TEXT_COLOR_CHOICES[1][0]
        elif self.number[:1] == '8':
            self.bg_color = self.BG_COLOR_CHOICES[8][0]
            self.text_color = self.TEXT_COLOR_CHOICES[1][0]
        elif self.number[:1] == '9':
            self.bg_color = self.BG_COLOR_CHOICES[9][0]
            self.text_color = self.TEXT_COLOR_CHOICES[0][0]
        return format_html(
            '<span style="background-color: {}; color: {};">{}</span>',
            self.bg_color,
            self.text_color,
            self.name,
        )


class Publication(models.Model):

    TYPEPUBLICATION_CHOICES = [
        ("B", "Books"),
        ("M", "Music"),
        ("F", "Film"),
        ("_", "Autre")
    ]
    isbn = models.CharField(max_length=13, null=True, blank=True)
    name = models.CharField(max_length=61)
    type_publication = models.CharField(
        max_length=1, choices=TYPEPUBLICATION_CHOICES, default='B')
    genre = models.CharField(max_length=35, null=True, blank=True)
    author = models.ForeignKey(Author, models.PROTECT)
    reference = models.CharField(
        max_length=61, null=True, blank=True, editable=False)
    dewey_number = models.ForeignKey(Dewey, models.PROTECT)
    date_publication = models.DateField(null=True, blank=True)
    nb_tracks_pages = models.IntegerField(null=True, blank=True)
    label_editor = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

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
