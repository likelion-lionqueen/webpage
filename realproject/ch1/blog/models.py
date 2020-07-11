from django.db import models
from django.utils import timezone

# Create your models here.

class Hashtag(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    #타이틀이라는 변수에서는 모델 안에 있는 문자 데이터를 처리하고
    #최대 길이는 200 지정
    pub_date = models.DateTimeField('date published')
    #날짜와 시간을 나타내는 데이터를 처리. 작성할 것도 지정
    body = models.TextField()
    #긴 문자로 된 데이터를 처리
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text


