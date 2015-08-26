# Aysin Oruz

from django.db import models
from django.utils import timezone

class Word(models.Model):
	title = models.CharField('title', max_length=256)

	def __unicode__(self):
		return self.title

class ShortUrl(models.Model):
	word = models.OneToOneField(Word, related_name='word_urls')
	url = models.URLField('Url', max_length=500)
	datetime = models.DateTimeField('Datetime', default=timezone.now)

	def __unicode__(self):
		return self.word.title

	class Meta:
		ordering = ['datetime']