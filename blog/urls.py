from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("article-detail/<slug:slug>", views.article_detail, name="article-detail"),
    path("article-list", views.article_list, name="article_list"),
    path("category-detail/<slug:slug>", views.category_detail, name="category_detail"),
    path("search", views.search, name="search_articles"),
    path("contact-us", views.contact_us, name="contact_us"),
    path("creat-article", views.create_article, name="creat_article"),
    path("dl-article/<int:id>", views.delete_article, name="dl_article"),
    path("edit-article/<int:id>", views.edit_article, name="edit_article"),
]
