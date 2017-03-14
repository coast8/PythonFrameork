import os, re
from sorl.thumbnail.base import ThumbnailBackend
from django.conf import settings


class SEOThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        split_path = re.sub(r'^%s%s?' % (source.storage.path(''), os.sep), '', source.name).split(os.sep)
        split_path.insert(-1, geometry_string)
        path = '%s' % os.sep.join(split_path)
        return '%s%s' % (settings.THUMBNAIL_PREFIX, path)