from django.db import models
from django.utils import timezone

class Article(models.Model):
	'''
	Defining the Article model
	'''
	title = models.CharField(max_length = 200)
	text = models.TextField()
	author = models.ForeignKey('auth.User')
	created_on = models.DateTimeField(default=timezone.now)
	published_on = models.DateTimeField(blank=True, null=True)

	def publish(self):
		'''
		Set the publishing time of an article 
		and persist it to the database
		'''
		self.published_on = timezone.now()
		self.save()

	def __str__(self):
		'''
		Return a string with the Artcile title
		'''
		return self.title