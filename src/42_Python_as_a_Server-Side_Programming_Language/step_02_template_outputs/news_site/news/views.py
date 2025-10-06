from django.shortcuts import render, get_object_or_404

from.models import Article, Comment


def articles(request):
    return render(request, 'news/articles.html',
        context={'articles' : Article.objects.all()})

def articles_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'news/articles_detail.html',
        context={'article' : article})
