from django.core.management.base import BaseCommand, CommandError
from blog.models import DesignPost
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
	arg = '<DesignPost_id DesignPost_id>'
	help = 'Custom Django admin command to publish a design article for blog'

	def handle(self, *args, **options):
		for DesignPost_id in args:
			try:
				article = DesignPost.objects.get(pk=int(DesignPost_id))
				if article.status == 'published':
					self.stdout.write('This article was already published')
				else:
					article.published_on  = timezone.now()
					article.status = 'published'
					article.save()
					self.stdout.write('Successfully published this article')
			except DesignPost.DoesNotExist:
				raise CommandError ('That article does not exist')
				# Add logging
