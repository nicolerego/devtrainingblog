from django.core.management.base import BaseCommand, CommandError
from blog.models import CodePost

class Command(BaseCommand):
	help = 'Custom Django admin command to display unpublished code posts'

	def handle(self, *arg, **options):
		articles = CodePost.objects.filter(status="unpublished")
		count = len(articles)
		for article in articles:
			title = article.title 
			num = article.id
			self.stdout.write("{title} - Article id: {num}".format(title=title, num=num))
		if count == 0:
			self.stdout.write("All code articles have been publsihed")