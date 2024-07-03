from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def get_absolute_url(self):
        return reverse("blog:category_detail", args=[self.slug])

    def __str__(self):
        return self.title


class Article(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField("blog.Category", related_name="articles")
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    class Meta:
        ordering = ("-created",)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse("blog:article-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey("blog.Article", on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.author} - {self.body[:30]}"


class ContactUs(models.Model):
    title = models.CharField(max_length=100, null=True)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.text[:30]}"
