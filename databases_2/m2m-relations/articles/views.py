from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    ordering = '-published_at'
    context['object_list'] = Article.objects.prefetch_related('scopes', 'topics').order_by(ordering)
    return render(request, template, context)
