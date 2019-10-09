from django.contrib import admin

from LandingPage.models import Article, User
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#admin.site.register(models.Article)
#admin.site.register(models.User)
@admin.register(Article, User)
class VeiwAdmin(ImportExportModelAdmin):
    pass

