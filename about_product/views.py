import os
from .models import *
from contacts.models import *
from categories.models import *
from site_settings.models import *
from site_settings.models import *
from django.shortcuts import render


def about_product(request, lang='ru', slug=None, product_slug=None):
    data = {
        'page': 'about_product',
        'category_slug': str(slug),
        'slug': str(product_slug),
        'categories': Categories.objects.all(),
        'products': Product.objects.all(),
        'product_description': ProductDescription.objects.all(),
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
        'message': request.GET.get('message'),
    }
    if not contact_info['name'] or not contact_info['phone']:
        pass
    elif contact_info['name'] and contact_info['phone'] and not contact_info['message']:
        os.system(f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" ')
        data['success_sent'] = True
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--message "{contact_info["message"]}"')
        data['success_sent'] = True
    return render(request, 'about_product/index.html', context=data)

