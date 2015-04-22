from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.article_list),
	url(r'^blog/(?P<CodePost_id>\d+)/CodeArticle.html', views.CodeArticle, name='CodePostDetails'),
	url(r'^blog/(?P<DesignPost_id>\d+)/DesignArticle.html', views.DesignArticle, name='DesignPostDetails'),
]