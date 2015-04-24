from django.shortcuts import render
from django.utils import timezone
from .models import ArticleInfo
from .models import CodePost
from .models import DesignPost
from itertools import chain
from operator import attrgetter

def article_list(request):
	"""
	Querying the db to get articles that have been published,
	ordering them by published most recently and storing it 
	in each variable
	"""
	CodeArticles = CodePost.objects.filter(published_on__lte=timezone.now()).order_by('-published_on')
	DesignArticles = DesignPost.objects.filter(published_on__lte=timezone.now()).order_by('-published_on')

	AllArticles = sorted(
		chain(CodeArticles, DesignArticles),
		key=attrgetter('published_on'))

	"""
	Takes request and returns method render
	to put together article_list template
	"""
	# return render(request, 'blog/article_list.html', {'CodeArticles': CodeArticles, 'DesignArticles': DesignArticles })
	return render(request, 'blog/article_list.html', {'AllArticles': AllArticles})
def CodeArticle(request, CodePost_id):
	"""
	Defines a variable to store a single article.
	This is used in the template for CodePost details.
	"""
	CodeArticle = CodePost.objects.get(pk= CodePost_id)
	# CodeRelated = CodePost.objects.all().Random().sample(range(0,last),2) 
	return render(request, 'blog/CodeArticle.html', {'CodeArticle': CodeArticle})

def DesignArticle(request, DesignPost_id):
	"""
	Defines a variable to store a single article. 
	This is used in the template for the DesignPost details.
	"""
	DesignArticle = DesignPost.objects.get(pk= DesignPost_id)
	return render(request, 'blog/DesignArticle.html', {'DesignArticle': DesignArticle})
