from django.contrib import admin
from django.core.exceptions import ValidationError

from articles.models import Article, Tag, Scope
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        print(f'self.forms: {self.forms}')
        counter = 0
        for form in self.forms:
            print(f'form.cleaned_data: {form.cleaned_data}')
            print(f'form.cleaned_data.keys(): {form.cleaned_data.keys()}')
            if 'is_main' not in form.cleaned_data.keys() and list(form.cleaned_data) != []:
                raise ValidationError('Укажите основной раздел')
            else:
                if list(form.cleaned_data) != [] and form.cleaned_data['is_main']:
                    counter +=1
                    print(counter)
        if counter > 1:
            raise ValidationError('Основным может быть только один раздел')
        else:
            return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

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
