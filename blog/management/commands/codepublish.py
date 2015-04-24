from django.core.management.base import BaseCommand, CommandError
from blog.models import CodePost
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger('django.blog')

class Command(BaseCommand):
    arg = '<CodePost_id CodePost_id>'
    help = 'Custom Django admin command to publish a code article for blog'

    def handle(self, *args, **options):
        for CodePost_id in args:
            try:
                article = CodePost.objects.get(pk=int(CodePost_id))
                if article.status == 'published':
                    self.stdout.write('This article was already published')
                else:
                    article.published_on  = timezone.now()
                    article.status = 'published'
                    article.save()
                    self.stdout.write('Successfully published this article')
            except CodePost.DoesNotExist:
                logger.info("The article requested does not exist")

                raise CommandError ('That article does not exist')


            
