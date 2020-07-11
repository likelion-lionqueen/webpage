from django.contrib import admin

# Register your models here.
from .models import Blog, Comment, Hashtag
#같은 폴더 내에 있는 모델 안에서 블로그 객체 가져오기

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Hashtag)
#admin sitedp 등록해라