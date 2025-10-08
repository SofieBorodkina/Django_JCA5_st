from django.urls import path
from .views import articles, unique ,article_main

urlpatterns = [
    path('',article_main, name="main_article"),    
    path('5/',unique, name="unique_article"),
    path('<int:article_id>/',articles),
    path('<int:article_id>/<slug:article_name>/',articles)
]