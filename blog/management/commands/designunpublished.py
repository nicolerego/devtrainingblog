from django.core.management.base import BaseCommand, CommandError
from blog.models import DesignPost

class Command(BaseCommand):
	"""
	Creating custom command to display unpublished articles and their id
	"""
	help = 'Custom Django admin command to display unpublished design posts'

	def handle(self, *arg, **options):
		"""
        Searches for unpublished posts and returns their title and id if found 
        """
		articles = DesignPost.objects.filter(status="unpublished")
		count = len(articles)
		for article in articles:
			title = article.title 
			num = article.id
			self.stdout.write("{title} - Article id: {num}".format(title=title, num=num))
		if count == 0:
			self.stdout.write("All code articles have been publsihed")