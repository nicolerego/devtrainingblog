from django.shortcuts import render

def article_list(request):
	'''
	Takes request and returns method render
	to put together article_list template
	'''
	
	return render(request, 'blog/article_list.html', {})
