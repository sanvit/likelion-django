from django.urls import path
import hello.views

urlpatterns = [
    path('', hello.views.home, name='home'),
    path('create', hello.views.postcreate, name='postcreate'),
    path('new/', hello.views.postnew, name='postnew'),
    path('detail/<int:post_id>', hello.views.detail,name='detail'),
    path('edit/<int:post_id>', hello.views.postedit,name='postedit'),
    path('update/<int:post_id>', hello.views.postupdate,name='postupdate'),
    path('delete/<int:post_id>', hello.views.postdelete,name='postdelete'),
]
