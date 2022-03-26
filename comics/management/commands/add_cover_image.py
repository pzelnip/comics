"""

THIS IS DEPRECATED AND NO LONGER NEEDED.

Now covers are just placed in static/covers, and will be loaded
if present.
"""


from contextlib import suppress
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from django.conf import settings
from comics.models import Comic


BASE_PATH = f"{settings.MEDIA_ROOT}/comic_covers"


def add_cover_image(issue):
    comic = Comic.objects.get(issue_number=issue)
    cover_image = Path(f"{settings.MEDIA_ROOT}/comic_covers/xmen_{issue}.jpg")
    if cover_image.exists():
        with cover_image.open(mode="rb") as fobj:
            comic.cover = File(fobj, name=cover_image.name)
            comic.save()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("source_dir", nargs="+", type=str)

    # pylint: disable=unused-argument
    def handle(self, *args, **kwargs):
        for source in kwargs["source_dir"]:
            for path in Path(source).glob("xmen_*.jpg"):
                print(f"Found image: {path}")
                with suppress(ValueError):
                    issue = int(path.name[5:-4])
                    add_cover_image(issue)
                    print(f"Updated image for {issue}")
