from django.test import TestCase
from projects.models import ShortUrl, Word
from django.core.urlresolvers import reverse
from projects.words import clean_word, save_word
from projects.views import *
from django.core import management


class MainViewTests(TestCase):
    def test_home_view(self):
        """
        Test home view
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class RedirectTests(TestCase):
    def setUp(self):
        Word.objects.create(title="apple")

    def test_redirect(self):
        """Test redirect 301, 404"""

        word_object = Word.objects.all()[0]

        short_url = ShortUrl.objects.create(word=word_object, url='http://google.com')

        #check 301 redirect
        response = self.client.get(reverse('redirect',
                                   args=(short_url.word,)))

        self.assertRedirects(response, 'http://google.com', status_code=301, target_status_code=200, msg_prefix='')

        #check wrong url
        response = self.client.get(reverse('redirect',
                                   args=('wrongurl',)))
        self.assertEqual(response.status_code, 404)


class ImportWordsTests(TestCase):

    def test_clean_word(self):
        """test method clean word"""
        word = "A$! p&p#l@' e"
        self.assertEqual(clean_word(word), 'apple')

    def test_save_word(self):
        """test save new word and check now doubles"""

        word = "apple"
        word_object = save_word(word)

        self.assertEqual(word_object.title, 'apple')
        self.assertEqual(Word.objects.all().count(), 1)
        self.assertEqual(Word.objects.all()[0].title, 'apple')

        #save one more and check no doubles
        save_word(word)
        self.assertEqual(Word.objects.all().count(), 1)

        #test new word don't delete previous ShortUrl
        ShortUrl.objects.create(word=word_object, url='http://google.com')
        save_word(word)
        self.assertEqual(ShortUrl.objects.all().count(), 1)
        #
    def test_import_words(self):
        """test count import words"""
        #first import
        management.call_command('import_words')

        count = Word.objects.all().count()

        #second import
        management.call_command('import_words')

        #check count
        self.assertEqual(Word.objects.all().count(), count)


class GenerateURLTests(TestCase):
    def test_find_word_by_url(self):
        """test find word"""
        Word.objects.create(title="apple")
        Word.objects.create(title="orange")

        self.assertEqual(find_word_by_url('http://apple.com').title, "apple")
        self.assertEqual(find_word_by_url('http://google.com/apple').title, "apple")
        self.assertEqual(find_word_by_url('http://google.com/apple-page').title, "apple")
        self.assertEqual(find_word_by_url('http://google.com/page/apple').title, "apple")
        self.assertEqual(find_word_by_url('http://google.com/ApPle').title, "apple")

        self.assertNotEqual(find_word_by_url('http://google.com/page/'), None)

    def test_get_reuse_word(self):
        """test get reuse word"""
        word_object = Word.objects.create(title="apple")
        ShortUrl.objects.create(word=word_object, url='http://apple.com')

        word_object = Word.objects.create(title="orange")
        ShortUrl.objects.create(word=word_object, url='http://orange.com',
                                datetime=timezone.now()+timezone.timedelta(minutes=61))

        self.assertEqual(find_word_by_url('http://google.com/grape'), "apple")

    def test_generate_url(self):
        word_object = Word.objects.create(title="apple")
        short_url = str(settings.HOST) + "/" + (str(word_object.title))

        #check return short_url
        self.assertEqual(generate_url('http://apple.com'), short_url)

        #check reuse word
        self.assertEqual(generate_url('http://google.com/apple-page'), short_url)



















