from django.contrib import admin
from .models import Article, Tag, Scope


class ScopeInline(admin.TabularInline):
    model = Scope

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['tag', 'article', 'is_main']
