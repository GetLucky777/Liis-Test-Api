from django.contrib import admin

from liis_api.articles.models import Article

admin.site.register([Article, ])
