from django.shortcuts import render
from models import Word, ShortUrl
from forms import UrlForm
from django.http import Http404
from django.utils import timezone
from urlparse import urlparse
from django.views.generic import RedirectView
from django.conf import settings


def home(request):
    #Home page

    context = {}
    if not check_words_load():
        context['msg'] = 'First, load the words.'
    if request.method == 'POST' and check_words_load():
        form = UrlForm(request.POST)
        if form.is_valid():
            short_url = generate_url(form.cleaned_data['url'])
            context['short_url'] = short_url
            context['result'] = True
    else:
        form = UrlForm()
    context['form'] = form
    return render(request, 'home.html', context)


def generate_url(url_link):
    # Generating short url

    # check if the url already exists
    short_url_object = get_short_object_by_url(url_link)
    if short_url_object:
        return get_short_url_path(short_url_object)

    word = find_word_by_url(url_link)

    if word:
        return get_short_object(word, url_link)
    else:
        return None


def find_word_by_url(url):

    url_parse = urlparse(url)

    # try by host
    host = url_parse.netloc
    url_parts = host.split('.')
    word = find_word_by_parts(url_parts)
    if word:
        return word

    # try by path
    url_parts = url_parse.path.split('/')
    word = find_word_by_parts(url_parts)
    if word:
        return word

    # get random word
    used_words = ShortUrl.objects.values_list('word')
    words = Word.objects.exclude(pk__in=used_words).order_by("?")
    if words:
        return words[0]
    else:
        # reuse word
        word = ShortUrl.objects.all()[0].word.title
        return word


def get_short_object_by_url(url):
    try:
        short_url_object = ShortUrl.objects.get(url=url)
        return short_url_object
    except ShortUrl.DoesNotExist:
        return None


def get_short_object(word, url_link):
    # create or get ShortUrl object by word and return short link 

    short_url_objects = ShortUrl.objects.filter(word__title=word)
    if short_url_objects:
        short_url_object = short_url_objects[0]
        # reuse here
        short_url_object.url = url_link
        short_url_object.datetime = timezone.now()
        short_url_object.save()
    else:
        # new item
        short_url_object = ShortUrl(word=word, url=url_link)
        short_url_object.save()

    return get_short_url_path(short_url_object)


def find_word(word):
    used_words = ShortUrl.objects.values_list('word')
    word_filter = Word.objects.filter(title=word.lower()).exclude(title__in=used_words)
    if word_filter.exists():
        return word_filter[0]


def find_word_by_parts(url_parts):

    for part in url_parts:
        if part != "" and part:
            if "-" in part:
                part_items = part.split("-")
                for part_item in part_items:
                    word = find_word(part_item)
                    if word:
                        return word

            if find_word(part):
                word = find_word(part)
                if word:
                    return word
    return None


class ShortUrlRedirectView(RedirectView):
    def dispatch(self, *args, **kwargs):
        short_url = kwargs.get('short_url')
        if short_url:
            try:
                short_url = ShortUrl.objects.get(word__title=short_url)
            except ShortUrl.DoesNotExist:
                raise Http404
            if short_url:
                # set the redirect long URL
                self.url = short_url.url

        return super(ShortUrlRedirectView, self).dispatch(*args, **kwargs)


def get_short_url_path(short_url_object):
    site = settings.HOST
    short_url = str(site) + "/" + (str(short_url_object.word))
    return short_url


def check_words_load():
    if Word.objects.all().count() == 0:
        return False
    else:
        return True
