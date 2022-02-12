import os
from .models import *
from contacts.models import *
from site_settings.models import *
from django.shortcuts import render
from site_settings.models import *
from reviews.models import *
from categories.models import *
from random import choice


def home(request, lang='ru'):
    search_query = request.GET.get('search-ru')
    search_query_uz = request.GET.get('search-uz')
    data = {
        'page': 'home',
        'comments': Comments.objects.all(),
        'benefits': Benefits.objects.all(),
        'meta': MetaTags.objects.all(),
        'favicons': Favicon.objects.all(),
        'head_tags': HeadTags.objects.all(),
        'lang': lang,
        'contact_info': {
            'phones': Phone.objects.all(),
            'emails': EMail.objects.all(),
            'addresses': Address.objects.all(),
            'social': SocialLink.objects.all()
        },
    }
    contact_info = {
        'name': request.GET.get('name'),
        'phone': request.GET.get('phone'),
        'company': request.GET.get('company'),
        'message': request.GET.get('message'),
    }
    if not contact_info['name'] or not contact_info['phone'] or not contact_info['message']:
        pass
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--company "{contact_info["company"]}" --message "{contact_info["message"]}"')
        data['success_sent'] = True
    if search_query:
        data['founded'] = []
        for product in Product.objects.all():
            if search_query.lower() in product.name.lower():
                data['founded'].append(product)
        return render(request, 'search-result.html', context=data)
    elif search_query_uz:
        data['founded'] = []
        for product in Product.objects.all():
            if search_query_uz.lower() in product.name_uz.lower():
                data['founded'].append(product)
        return render(request, 'search-result.html', context=data)

    data['random_categories'] = []
    data['random_products'] = []
    category_array = list(Categories.objects.all())
    product_array = list(Product.objects.all())

    if len(category_array) >= 6:
        while len(data['random_categories']) < 6:
            random_obj = choice(category_array)
            if random_obj not in data['random_categories']:
                data['random_categories'].append(random_obj)
    else:
        data['random_categories'] = 'no'

    if len(product_array) >= 6:
        while len(data['random_products']) < 5:
            random_obj = choice(product_array)
            if random_obj not in data['random_products']:
                data['random_products'].append(random_obj)
    elif len(product_array) >= 5:
        while len(data['random_products']) < 5:
            random_obj = choice(product_array)
            if random_obj not in data['random_products']:
                data['random_products'].append(random_obj)
    else:
        data['random_products'] = 'no'
    print(f"\n\n\n\n{data['random_categories']}\n\n\n\n")
    return render(request, 'home/index.html', context=data)
