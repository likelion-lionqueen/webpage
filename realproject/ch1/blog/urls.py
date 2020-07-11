from django.urls import path
import blog.views

app_name = 'blog'
urlpatterns = [


path('blog/<int:blog_id>', blog.views.detail, name = "detail"),
path('blog/new/',blog.views.new, name="new"),
path('blog/create/',blog.views.create, name="create"),
path('blog/delete/<int:blog_id>',blog.views.delete, name="delete"),
path('blog/edit/<int:blog_id>',blog.views.edit, name="edit"),
path('blog/update/<int:blog_id>',blog.views.update, name="update"),
path('<int:blog_id>/comment', blog.views.add_comment_to_post, name='add_comment_to_post'),
path('blog/people_detail/', blog.views.people_detail, name ="people_detail"),

]