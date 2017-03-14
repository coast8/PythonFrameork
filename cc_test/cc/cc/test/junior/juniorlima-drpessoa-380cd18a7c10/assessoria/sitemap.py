from django.contrib.sitemaps import Sitemap
from assessoria.models import Postagem

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Postagem.objects.filter(publicar=True)

    def lastmod(self, obj):
        return obj.data_publicacao

