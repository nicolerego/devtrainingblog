from django.core.management.base import BaseCommand, CommandError
from blog.models import DesignPost
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
	arg = '<DesignPost_id DesignPost_id>'
	help = 'Custom Django admin command to publish a design article for blog'

	def handle(self, *args, **options):
		# Needs to handle if article has already been published
		for DesignPost_id in args:
			try:
				article = DesignPost.objects.get(pk=int(DesignPost_id))
				article.published_on  = timezone.now()
			except DesignPost.DoesNotExist:
				raise CommandError ('That article does not exist')

			article.save()

			self.stdout.write('Successfully published this article')