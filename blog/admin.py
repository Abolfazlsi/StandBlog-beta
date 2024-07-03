from django.contrib import admin
from blog.models import Article, Category, Comment, ContactUs


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(ContactUs)
admin.site.register(Comment)
