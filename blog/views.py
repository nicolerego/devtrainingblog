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
	Defines a variable to store related articles, excludes
	displaying current article.
	"""
	CodeArticle = CodePost.objects.get(pk= CodePost_id)
	CodeRelateds = CodePost.objects.all().order_by('id').exclude(id = CodeArticle.id)[:3]
	
	return render(request, 'blog/CodeArticle.html', {'CodeArticle': CodeArticle, 'CodeRelateds': CodeRelateds })

def DesignArticle(request, DesignPost_id):
	"""
	Defines a variable to store a single article. 
	This is used in the template for the DesignPost details.
	Defines a variable to store related articles, excludes
	displaying curent article.
	"""
	DesignArticle = DesignPost.objects.get(pk= DesignPost_id)
	DesignRelateds = DesignPost.objects.all().order_by('id').exclude(id = DesignArticle.id)[:3]

	return render(request, 'blog/DesignArticle.html', {'DesignArticle': DesignArticle, 'DesignRelateds': DesignRelateds})
