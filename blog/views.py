from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog.models import Article, Category, Comment, ContactUs
from django.core.paginator import Paginator
from blog.forms import ContactUs, ContactUSForm, CreatArticleForm, ArticleEditForm
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        "article": article,
        "errors": []
    }

    if request.method == "POST":
        body = request.POST.get("body")
        parent_id = request.POST.get("parent_id")
        if request.user.is_anonymous:
            context["errors"].append("You are not logged in.")
            return render(request, "blog/article_detail.html", context)

        Comment.objects.create(body=body, article=article, author=request.user, parent_id=parent_id)

    return render(request, "blog/article_detail.html", context)


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get("page")
    objects_list = paginator.get_page(page_number)
    context = {
        "articles": objects_list
    }
    return render(request, "blog/article_list.html", context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()

    context = {
        "articles": articles
    }
    return render(request, "blog/article_list.html", context)


def search(request):
    q = request.GET.get("q")
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 1)
    page_number = request.GET.get("page")
    objects_list = paginator.get_page(page_number)

    context = {
        "articles": objects_list,
        "search_term": q
    }
    return render(request, "blog/article_list.html", context)


def contact_us(request):
    if request.method == "POST":
        form = ContactUSForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactUSForm()

    context = {
        "form": form
    }
    return render(request, "blog/contact_us.html", context)


def create_article(request):
    if request.method == "POST":
        form = CreatArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.auther = request.user
            new_article.image = form.cleaned_data.get("image")
            new_article.save()
            form.save_m2m()

            return redirect("home:home")
    else:
        form = CreatArticleForm()

    context = {
        "create_article": form,

    }
    return render(request, "blog/create_article.html", context)


def delete_article(request, id):
    dl_article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        dl_article.delete()
        return redirect("home:home")

    return render(request, "blog/article_detail.html", {"dl_article": dl_article})


def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleEditForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auther = request.user
            form.save()
            return redirect("home:home")
    else:
        form = ArticleEditForm(instance=article)

    return render(request, "blog/edit_article.html", {"form": form})

