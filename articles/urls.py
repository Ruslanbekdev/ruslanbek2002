from django.urls import path
from .views import form_created, home_view, detail_view, search_article, create_article, my_articles_view, article_update,article_delate
urlpatterns = [
    path('',home_view, name='base'),
    path('my-articles/', my_articles_view ),
    path('search/', search_article, name='search'),
    path('create/', create_article, name = 'create'),
    path('fcreate/', form_created, name='fcreate'),  
    path('delete/<slug:slug>/', article_delate, name = 'article_delate'),
    path('<slug:slug>/', detail_view, name='detail_index'),#<int:year>/<int:month>/<int:day>/ 
    path('update/<slug:slug>/', article_update, name = 'article_update'),
]
