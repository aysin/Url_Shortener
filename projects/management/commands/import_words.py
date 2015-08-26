# Aysin Oruz
# import modules

# take a look if you run to error
from django.core.management.base import BaseCommand, CommandError
from projects.words import import_words

class Command(BaseCommand):
	help = "Import words from the file"

	def handle(self, *args, **options):
		import_words()
		self.stdout.write("Success. File has been imported.")