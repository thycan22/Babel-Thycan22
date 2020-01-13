from django.core.management.base import BaseCommand
from catalog.utils import xls_reader
from catalog.models import Dewey


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--source", help=f"source file", default="scrap/La_Dewey_simplifiee.xls"
        )

    def handle(self, *args, **options):
        source = "scrap/La_Dewey_simplifiee.xls"
        if options["source"]:
            source = options["source"]

        rc = xls_reader(Dewey, source)
        print(f"Nb of dewey items processed {rc}")
