from collections import Counter

from django.shortcuts import render

counter_show = Counter()
counter_click = Counter()


def index(request):
    page_from = request.GET.get('from-landing', '')
    if page_from in ('original', 'test'):
        counter_click[page_from] += 1
    return render(request, 'index.html')


def landing(request):
    land_type = request.GET.get('ab-test-arg', 'original')
    if land_type not in ('original', 'test'):
        land_type = 'original'
    counter_show[land_type] += 1
    if land_type == 'original':
        return render(request, 'landing.html')
    elif land_type == 'test':
        return render(request, 'landing_alternate.html')


def stats(request):
    test_conv = 0
    orig_conv = 0
    if counter_show['test'] != 0:
        test_conv = round(counter_click['test'] / counter_show['test'], 2)
    if counter_show['original'] != 0:
        orig_conv = round(counter_click['original'] / counter_show['original'], 2)
    return render(request, 'stats.html', context={
        'test_conversion': test_conv,
        'original_conversion': orig_conv,
    })
