from django import forms
from django.core.validators import ValidationError
from blog.models import ContactUs, Article


class ContactUSForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your title",
                "style": "max-width: 300px"
            }),
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter your text"

            })
        }


class CreatArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["category", "title", "body", "image"]


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["category", "title", "body", "image"]
