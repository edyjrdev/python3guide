from django.shortcuts import render
from django.http import HttpResponse, Http404

from.models import Article, Comment


def articles(request):
    rows = []
    for m in Article.objects.all():
        rows.append("Article: '{}' from {}".format(
            m.title, m.timestamp.strftime('%d.%m.%Y at %H:%M')))
        rows.append('text: {}'.format(m.text))
        rows += ['', '-' * 30, '']
    response = HttpResponse('\n'.join(rows))
    response['Content-Type'] = 'text/plain'
    return response


def articles_detail(request, article_id):
    try:
        m = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404
 
    rows = [
        "Title: '{}' from {}".format(
            m.title, m.timestamp.strftime('%d.%m.%Y at %H:%M')),
        'Text: {}'.format(m.text),
        '', '-' * 30,
        'Comments:', '']
    rows += ['{}: {}'.format(c.author, c.text) 
               for c in m.comment_set.all()]
    response = HttpResponse('\n'.join(rows))
    response['Content-Type'] = 'text/plain'
    return response
