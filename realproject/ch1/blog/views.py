from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog,Hashtag
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm

# Create your views here.

def home(request):
    blogs = Blog.objects
    #블로그 모델 안의 데이터를 블로그스 라는 변수에 넣어주기
    return render(request, 'home.html', {'blogs': blogs})
    #blogs 자료를 가져올 때 blogs라는 이름으로 가져오겠다

def detail(request, blog_id): 
    blog_detail = get_object_or_404(Blog, pk= blog_id)
    #blog_object = blog_id
    #블로그 n번째 객체를 받아줄 것임.
    hashtags = blog_detail.hashtag.all()
    return render( request, 'detail.html', {'blog':blog_detail, 'hashtags':hashtags})
    #디테일 html에 띄우기

def people_detail(request):
    return render(request, 'people_detail.html')

def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    hashtags = request.GET['hashtags']
    hashtag = hashtags.split(",")
    for tag in hashtag:
        #ht = Hashtag()
        #ht.name = tag
        #ht.save()
        #blog.hashtag.add(ht)
        ht = Hashtag.objects.get_or_create(name = tag)
        blog.hashtag.add(ht[0])

    return redirect('/blog/blog/'+str(blog.id))

def delete(request, blog_id):
    blogs = Blog.objects.get(pk= blog_id)
    blogs.delete()
    return redirect('home')

def edit(request,blog_id):
    #블로그 아이디라는 이름의 변수를 통해 게시물 번호가 전달됨
    blog_edit = Blog.objects.get(pk=blog_id)
    #모델에서 블로그 아이디 번호를 가진 게시물을 불러와서 블로그에딧에 저장
    return render(request, 'edit.html', {'blog': blog_edit})
    #블로그에딧에 저장된 값이 블로그의 이름으로 전달됨.

@csrf_exempt
def update(request, blog_id):
    blog = Blog.objects.get(pk= blog_id)
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('home')


def add_comment_to_post(request, blog_id):
    blog = get_object_or_404(Blog, pk= blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = blog
            comment.save()
            return redirect('blog:detail', blog_id)
    else:
            form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})