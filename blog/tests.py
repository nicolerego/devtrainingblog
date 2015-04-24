from django.test import TestCase
from models import CodePost
from models import DesignPost
from django.utils import timezone
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
from django.db import models

# Test that author is the superuser

# Test that design posts have photos while code posts do not

# Test that most recent articles appear first
# make a new article, text if it appears first 

class CodePostCase(TestCase):
	# def setUp(self):
	# 	CodePost.objects.create(
	# 		title="A Post About Code", 
	# 		author=User.objects.get(pk=1),
	# 		created_on=timezone.now()
	# 		)

	def test_if_articles_order(self):
		articles = CodePost.objects.filter(status='published').order('-published_on')
		first = articles[0]
		print first


