import os
from .models import *
from contacts.models import *
from site_settings.models import *
from django.shortcuts import render
from site_settings.models import *


def contacts(request, lang='ru'):
    data = {
        'page': 'contacts',
        'phones': Phone.objects.all(),
        'emails': EMail.objects.all(),
        'social_links': SocialLink.objects.all(),
        'addresses': Address.objects.all(),
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
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--message "{contact_info["message"]}"')
        data['success_sent'] = True
    return render(request, 'contacts/index.html', context=data)
