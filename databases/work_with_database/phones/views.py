from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort', 'default')
    template = 'catalog.html'
    context = dict()
    sort_types = {'default': 'id',
                  'names': 'name',
                  'price_inc': 'price',
                  'price_dec': '-price'}
    context['phones'] = Phone.objects.order_by(sort_types[sort])
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = dict()
    context['phone'] = Phone.objects.get(slug=slug)
    return render(request, template, context)
