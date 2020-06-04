from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import ScrappedNews, NewsPost, Search, Subscriber

#Customizing Admin Page with ModelAdmin
#first inherit ImportExportModelAdmin and then admin.ModelAdmin
#otherwise there will be error in inheritance
#ImportExportModelAdmin is for showing import and export options in Django Administration
#admin.ModelAdmin is for displaying lists, links and filter options
class ScrappedNewsModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["title", "description", "author", "category", "posted", "scrapped"]
    list_display_links = ["description"]
    list_filter = ["author", "category", "posted","scrapped"]
    search_fields = ["title", "content", "user", "category"]
    class Meta:
        model = ScrappedNews
    
class NewsPostModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["user", "title", "content", "timestamp", "publish_date", "updated"]
    list_display_links = ["content"]
    # list_editable = ["title"]
    list_filter = ["user", "timestamp", "updated"]
    search_fields = ["user", "title", "content"]
    class Meta:
        model = NewsPost

class SearchModelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["user", "search", "timestamp"]
    class Meta:
        model = Search

# Register your models here.
admin.site.register(ScrappedNews, ScrappedNewsModelAdmin) #Registering AllNewsModelAdmin Class
admin.site.register(NewsPost, NewsPostModelAdmin) #Registering NewsPostModelAdmin Class
admin.site.register(Search, SearchModelAdmin) #Registering SearchModelAdmin Class
admin.site.register(Subscriber)