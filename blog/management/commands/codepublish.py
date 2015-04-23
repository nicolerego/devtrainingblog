from django.core.management.base import BaseCommand, CommandError
from blog.models import CodePost
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
	arg = '<CodePost_id CodePost_id>'
	help = 'Custom Django admin command to publish a code article for blog'

	def handle(self, *args, **options):
		# Needs to handle if article has already been published
		for CodePost_id in args:
			try:
				article = CodePost.objects.get(pk=int(CodePost_id))
				article.published_on  = timezone.now()
			except CodePost.DoesNotExist:
				raise CommandError ('That article does not exist')

			article.save()

			self.stdout.write('Successfully published this article')
		

	# def handle(self, *args, **options):
	# 	# WORKS FOR DOES NOT EXIST AND PUBLISH
	# 	# Needs to handle if article has already been published
	# 	for CodePost_id in args:
	# 		try:
	# 			article = CodePost.objects.get(pk=int(CodePost_id))

	# 			if article.published_on == nul:
	# 				article.published_on  = timezone.now()
	# 				article.save()
	# 				self.stdout.write('Successfully published this article')
	# 			else:
	# 				self.stdout.write('That article has already been published')
				
	# 		except CodePost.DoesNotExist:
	# 			raise CommandError ('That article does not exist')


	# def handle(self, *args, **options):
	# 	# 	WORKS FOR ALREADY PUBLISHED AND PUBLISH
	# 	for CodePost_id in args:
	# 		CodeArticle = CodePost.objects.get(pk= CodePost_id)
	# 		if CodeArticle.published_on == 'nil':
	# 			try:
	# 				article = CodePost.objects.get(pk=int(CodePost_id))
	# 				article.published_on  = timezone.now()
	# 			except self.DoesNotExist:
	# 				raise CommandError ('That article does not exist')

	# 			article.save()

	# 			self.stdout.write('Successfully published this Code article')
	# 		else: 
	# 			self.stdout.write('That article has already been published')


	# def handle(self, *args, **options):
	# 	for CodePost_id in args:
	# 		CodeArticle = CodePost.objects.get(pk= CodePost_id)
	# 		if CodeArticle.published_on == 'null':
	# 			article = CodePost.objects.get(pk=int(CodePost_id))
	# 			article.published_on  = timezone.now()
	# 			article.save()
	# 			self.stdout.write('Successfully published this Code article')
	# 		elif CodeArticle.published_on != 'null': 
	# 			# raise CommandError ('That article does not exist')
	# 			self.stdout.write('That article has already been published')
	# 			# self.stdout.write('That article does not exist')
	# 		else:
	# 			# self.stdout.write('That article has already been published')
	# 			self.stdout.write('That article does not exist')
