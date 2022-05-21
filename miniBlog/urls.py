from django.urls import path,include
from .views import *
from froala_editor import views

urlpatterns = [
    path('',home,name='home'),
    path('login',signin,name='login'),
    path('signup',signup,name='signup'),
    path('logout',signout,name='signout'),
    path('add-blog',addBlog,name='addblog'),
    path('blog-detail<slug>',blogDetail,name='blog_detail'),
    path('see-blogs',seeBlogs,name='seeblogs'),
    path('update-blog<slug>',updateBlog,name='updateblog'),
    path('delete-blog<slug>',deleteBlog,name='deleteblog'),
]
