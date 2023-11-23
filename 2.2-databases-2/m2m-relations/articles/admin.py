from django.contrib import admin
from django.core.exceptions import ValidationError

from articles.models import Article, Tag, Scope
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        print(f'self.forms: {self.forms}')
        counter = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data.keys():
                if form.cleaned_data['is_main']:
                    counter += 1
        if counter == 1:
            return super().clean()
        elif counter < 1:
            raise ValidationError('Укажите основной раздел')
        else:
            raise ValidationError('Основным может быть только один раздел')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['tag', 'article', 'is_main']
