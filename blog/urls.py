from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(
		regex=r'^$', 
		view=views.article_list
		),
	url(
		regex=r'^blog/(?P<CodePost_id>\d+)/CodeArticle.html', 
		view=views.CodeArticle, 
		name='CodePostDetails'),
	url(
		regex=r'^blog/(?P<DesignPost_id>\d+)/DesignArticle.html', 
		view=views.DesignArticle, 
		name='DesignPostDetails'),
]