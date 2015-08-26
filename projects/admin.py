#Aysin Oruz

from django.contrib import admin
from models import ShortUrl, Word
from projects.words import import_words

def import_words_file(modeladmin, request, queryset):
	import_words()

import_words.short_description = "Import words.txt file"

class WordAdmin(admin.ModelAdmin):
	actions = [import_words_file]
	search = ('title', )

class ShortUrlAdmin(admin.ModelAdmin):
	display = ('url', 'datetime', )

admin.site.register(Word, WordAdmin)
admin.site.register(ShortUrl, ShortUrlAdmin)