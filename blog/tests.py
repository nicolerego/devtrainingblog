from django.test import TestCase
from models import CodePost
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class CodePostCase(TestCase):
	"""
	Defining a case to test for CodePost model
	"""
	def setUp(self):
		"""
		Setting up a user and creating three
		posts with different published times
		"""
		super(CodePostCase, self).setUp()
		User.objects.create_superuser(
			username='admin', 
			password='123',
			email=''
			)
		self.post= CodePost.objects.create(
			title="New Post About Code", 
			created_on=timezone.now(), 
			published_on=timezone.now(), 
			status='published',
			author_id = 1
			)
		self.post= CodePost.objects.create(
			title="Another Code Post", 
			created_on=timezone.now(), 
			published_on=timezone.now() - timedelta(days=3), 
			status='published',
			author_id = 1
			)
		self.post= CodePost.objects.create(
			title="The Millionth Post About Code", 
			created_on=timezone.now(), 
			published_on=timezone.now() - timedelta(days=5), 
			status='published',
			author_id = 1
			)
		CodePost.author_id = 1

	def test_if_articles_order(self):
		"""
		Testing the order articles are displayed in, 
		expecting the most recenlty published to be first
		"""
		articles = CodePost.objects.filter(published_on__lte=timezone.now()).order_by('-published_on')
		first = articles[0]
		first = '{first}'.format(first=first)
		self.assertEqual(first, 'New Post About Code')

	def test_CodePost_creation(self):
		"""
		Testing for post creation
		"""
		post = CodePost.objects.get(pk=1)
		self.assertTrue(isinstance(post, CodePost))
		self.assertEqual(post.__str__(), post.title)

class ArticleListViewTestCase(TestCase):
	"""
	Defining a case to test for the artcle list template
	"""
	def test_index(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)