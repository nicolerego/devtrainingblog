from django.db import models
from django.utils import timezone

class ArticleInfo(models.Model):
	'''
	Defines a base model for all articles
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

	class Meta:
		abstract = True


class CodePost(ArticleInfo):
	'''
	Defining CodePost, inheriring properties of 
	ArticleInfo. CodePosts allow for a link and description
	of link.
	'''
	link = models.TextField()
	description = models.TextField()


class DesignPost(ArticleInfo):
	'''
	Defining DesignPost ,inheriring properties of 
	ArticleInfo. DesignPosts allow for an image to be uploaded/
	added to the article.
	'''
	photo = models.ImageField(upload_to="images/", blank=True, null=True)


# class Comment(models.Model):
# 	post = models.ForeignKey('ArticleInfo')
# 	name = models.CharField(max_length = 50)
# 	comment = models.TextField()
# 	created_on = models.DateTimeField(default=timezone.now)
