from django.contrib import admin
from .models import Category
from mptt.admin import DraggableMPTTAdmin




class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)


admin.site.register(Category, CategoryAdmin)
