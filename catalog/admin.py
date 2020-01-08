from django.contrib import admin
from .models import Author, Publication, Dewey


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'reference',
                    'isbn',
                    'type_publication',
                    'genre',
                    'author',
                    'dewey_number',
                    'date_publication',
                    'label_editor')

    list_reference = (('type_publication', 'dewey_number'),
                      ('isbn',
                       'reference'))
    list_publication = ('name', 'author', 'label_editor',
                        )
    list_details = ('date_publication', 'nb_tracks_pages',
                    'content',
                    'image_url', 'image_file')

    fieldsets = (
        ('Reference', {
            'fields': list_reference
        }),
        ('Publication', {
            'fields':  list_publication
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': list_details
        }),
    )

    radio_fields = {"type_publication": admin.HORIZONTAL}
    readonly_fields = ('reference',)


class AuthorAdmin(admin.ModelAdmin):
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
        ('Identité', {
            'fields': list_identity
        }),
        ('Naissance', {
            'fields':  list_birth
        }),
        ('Décès', {
            'classes': ('collapse',),
            'fields': list_death
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': list_details
        }),
    )
    readonly_fields = ('century_birth',)


class DeweyAdmin(admin.ModelAdmin):
    list_display = ('number',
                    'name',
                    'set_dewey_color_publication',
                    )


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)
