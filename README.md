# Developer Blog
Django developer training blog. Built on Ubuntu with Django 1.7

#### Models
* ArticleInfo
* CodePost
* DesignPost

CodePost and DesignPost inherit properties of ArticleInfo 

#### Django-admin Commands
```
$ python manage.py codeunpublished
```
* codeunpublished and designunpublished - Return a list of titles and corresponding ids for articles which have not been published. Requires no arguments.
```
$ python manage.py codepublish 5
```
* codepublish {id} and designpublish {id} - Publishes an article. Requires an article id to publish. 
