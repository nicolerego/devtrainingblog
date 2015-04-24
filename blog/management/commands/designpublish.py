from django.core.management.base import BaseCommand, CommandError
from blog.models import DesignPost
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger('django.blog')

class Command(BaseCommand):
	"""
    Creating custom admin command to publish an article
    """
	arg = '<DesignPost_id DesignPost_id>'
	help = 'Custom Django admin command to publish a design article for blog'

	def handle(self, *args, **options):
		"""
        Param requires the post id. If the article has already been published or 
        does not exist, returns a statement indicating each. If article has not
        been published, will publish now and return a success message.
        """
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
                logger.info("The article requested does not exist")
				
				raise CommandError ('That article does not exist')
