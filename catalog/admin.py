from django.contrib import admin
from .models import Author, Publication, Dewey
from django.utils.translation import gettext as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PublicationResource(resources.ModelResource):

    class Meta:
        model = Publication


class AuthorResource(resources.ModelResource):

    class Meta:
        model = Author


class DeweyResource(resources.ModelResource):

    class Meta:
        model = Dewey


class PublicationAdmin(ImportExportModelAdmin):

    list_display = ('name',
                    'reference',
                    'isbn',
                    'type_publication',
                    'genre',
                    'author',
                    'dewey_number',
                    'date_publication',
                    'label_editor',)

    list_reference = (('type_publication', 'dewey_number'),
                      ('isbn',
                       'reference'))
    list_publication = ('name', 'author', 'label_editor',
                        )
    list_details = ('date_publication', 'nb_tracks_pages',
                    'content',
                    'image_url', 'image_file',)

    fieldsets = (
        (_('Reference'), {
            'fields': list_reference
        }),
        (_('Publication'), {
            'fields':  list_publication
        }),
        (_('Details'), {
            'classes': ('collapse',),
            'fields': list_details
        }),
    )

    radio_fields = {"type_publication": admin.HORIZONTAL}
    readonly_fields = ('reference',)
    search_fields = ['name', 'reference', 'dewey_number__number', 'dewey_number__name',
                     ]
    autocomplete_fields = ['author', 'dewey_number', ]
    list_filter = ('dewey_number__number', 'author__last_name',)

    resource_class = PublicationResource


class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('last_name',
                    'first_name',
                    'date_birth',
                    'century_birth'
                    )
    list_identity = [('last_name',
                      'first_name',)]
    list_birth = [('date_birth', 'place_birth', 'century_birth',)]
    list_death = [('date_died', 'place_died',)]
    list_details = [('content', 'image_url', 'image_file',)]

    fieldsets = (
        (_('Identité'), {
            'fields': list_identity
        }),
        (_('Naissance'), {
            'fields':  list_birth
        }),
        (_('Décès'), {
            'classes': ('collapse',),
            'fields': list_death
        }),
        (_('Details'), {
            'classes': ('collapse',),
            'fields': list_details
        }),
    )
    readonly_fields = ('century_birth',)
    search_fields = ('first_name', 'last_name', )
    list_filter = ('first_name', 'last_name',)
    resource_class = AuthorResource


class DeweyAdmin(ImportExportModelAdmin):
    list_display = ('number',
                    'name',
                    'set_dewey_color_publication',
                    )
    search_fields = ['name', 'number', ]
    list_filter = ('name',)
    resource_class = DeweyResource


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
