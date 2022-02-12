from .models import *
from contacts.models import *
from site_settings.models import *
from django.shortcuts import render
from site_settings.models import *
from .models import Comments


def reviews(request, lang='ru'):
    data = {
        'page': 'reviews',
        'comments': Comments.objects.all(),
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
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('message'):
            post = Comments()
            post.name = request.POST.get('name')
            post.message = request.POST.get('message')
            post.save()
    return render(request, 'reviews/index.html', context=data)

