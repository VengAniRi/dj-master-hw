from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        cnt = 0
        topics = set()
        for form in self.forms:
            if not form.cleaned_data:
                continue
            if form.cleaned_data['is_main']:
                cnt += 1
                if form.cleaned_data['DELETE']:
                    raise ValidationError('Нельзя удалить основной раздел')
            if not form.cleaned_data['DELETE']:
                if form.cleaned_data['topic'].topic in topics:
                    raise ValidationError('Уберите повторяющиеся разделы')
                topics.add(form.cleaned_data['topic'].topic)
        if cnt == 0:
            raise ValidationError('Укажите основной раздел')
        if cnt > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
