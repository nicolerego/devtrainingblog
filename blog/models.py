from django.db import models
from django.utils import timezone

class ArticleInfo(models.Model):
	"""
	Defines a base model for all articles
	"""
	title = models.CharField(max_length = 200)
	text = models.TextField()
	author = models.ForeignKey('auth.User')
	created_on = models.DateTimeField(default=timezone.now)
	published_on = models.DateTimeField(blank=True, null=True)
	status = models.TextField(default='unpublished')

	def publish(self):
		"""
		Sets the publishing time of an article 
		and gives it a status of published. It 
		then persists it to the database
		"""
		self.published_on = timezone.now()
		self.status = 'published'
		self.save()

	def __str__(self):
		"""
		Returns a string with the artcile title
		"""
		return self.title

	class Meta:
		abstract = True

class CodePost(ArticleInfo):
	"""
	Defining CodePost, inheriring properties of 
	ArticleInfo. CodePosts allow for a link and description
	of link.
	"""
	link = models.TextField()
	description = models.TextField()
	category = 'Code'


class DesignPost(ArticleInfo):
	"""
	Defining DesignPost ,inheriring properties of 
	ArticleInfo. DesignPosts allow for an image to be uploaded/
	added to the article.
	"""
	photo = models.ImageField(upload_to="static/blog/images", blank=True, null=True)
	category = 'Design'