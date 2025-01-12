from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly" # How often this content is updated.
    priority = 0.9  # How important this content is (1 = highest).

    def items(self):
        # Returns the list of objects to include in the sitemap.
        return Post.published.all()
    
    def lastmod(self, obj):
        # Returns the last modification date of each object.
        return obj.updated