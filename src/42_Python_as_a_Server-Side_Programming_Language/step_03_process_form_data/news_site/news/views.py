from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from.models import Article, Comment


def articles(request):
    return render(request, 'news/articles.html',
        context={'articles' : Article.objects.all()})


def articles_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
 
    if 'save_comment' in request.POST:
        name = request.POST.get('visitor_name', '')
        text = request.POST.get('comment_text', '')
 
        if name and text:
            comment = article.comment_set.create(
                author=name, text=text)
            comment.save()
            return HttpResponseRedirect('.')
 
        else:
            return render(request, 'news/articles_detail.html',
                context={'article': article,
                         'error': 'Input your name and a comment.',
                         'visitor_name' : name, 'comment_text' : text})
 
    return render(request, 'news/articles_detail.html',
        context={'article' : article})
