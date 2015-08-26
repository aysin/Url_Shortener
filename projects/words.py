# Aysin Oruz

from models import Word
import re

def import_words():

	# Importing the words from the words.txt file
	word_list = open("words.txt", "r")
	Word.objects.all().delete()
	words = word_list.readlines()

	for line in words:
		line = clean_word(line)
		save_word(line)
		print line

	#close the file	
	word_list.close()


def clean_word(word):
	word = word.replace("'", "").rstrip().lower()
	word = re.sub(r'[^a-z0-9]', '', word)
	return word

def save_word(word):
	word_objects = Word.objects.filter(title=word)
	if not word_objects:
		word_object = Word(title=word)
		word_object.save()
	else:
		word_object = word_objects[0]
	return word_object