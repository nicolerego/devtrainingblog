from django.contrib import admin
from .models import ArticleInfo
from .models import CodePost
from .models import DesignPost

admin.site.register(CodePost)
admin.site.register(DesignPost)

