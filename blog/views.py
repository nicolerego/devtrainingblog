from django.shortcuts import render
from django.utils import timezone
from .models import ArticleInfo
from .models import CodePost
from .models import DesignPost

def article_list(request):
	'''
	Querying the db to get articles that have been published,
	ordering them by published most recently and storing it 
	in each variable
	'''
	CodeArticles = CodePost.objects.filter(published_on__lte=timezone.now()).order_by('published_on')
	DesignArticles = DesignPost.objects.filter(published_on__lte=timezone.now()).order_by('published_on')

	'''1
	Takes request and returns method render
	to put together article_list template
	'''
	return render(request, 'blog/article_list.html', {'CodeArticles': CodeArticles, 'DesignArticles': DesignArticles })

def CodeArticle(request, CodePost_id):
	'''
	Defines a variable to store a single article.
	This is used in the template for CodePost details.
	'''
	CodeArticle = CodePost.objects.get(pk= CodePost_id)
	return render(request, 'blog/CodeArticle.html', {'CodeArticle': CodeArticle})

def DesignArticle(request, DesignPost_id):
	'''
	Defines a variable to store a single article. 
	This is used in the template for the DesignPost details.
	'''
	DesignArticle = DesignPost.objects.get(pk= DesignPost_id)
	return render(request, 'blog/DesignArticle.html', {'DesignArticle': DesignArticle})
