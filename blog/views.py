from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()

    return render(request, "./blog/titles.html", {"blogs": blogs})


def blog_articles(request, articles_id):
    # articles = BlogArticles.objects.get(id=articles_id)
    articles = get_object_or_404(BlogArticles, id=articles_id)
    pub = articles.publish
    return render(request, "./blog/content.html", {"artcles": articles, "publish": pub})
