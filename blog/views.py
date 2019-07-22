from django.shortcuts import render, Http404, get_object_or_404
from django.core.paginator import Paginator

from blog.models import Article, Category


def home_page(request):
    args = {
        'categories': Category.objects.all(),
    }

    return render(request, 'index.html', args)


def blog_home(request):
    # blog main page
    article_list = Article.objects.all().order_by('-created')
    categories = Category.objects.all()

    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    args = {
        'articles': articles,
        'categories': categories,
        'page_title': 'Articles'
    }

    return render(request, 'blog/home.html', args)


def blog_category(request, code):
    # category content view
    category = get_object_or_404(Category, pk=code)
    article_list = category.article_set.all()

    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    args = {
        'articles': articles,
        # 'articles': Article.objects.filter(category=category),
        'categories': Category.objects.all(),
        'page_title': category.name
    }

    return render(request, 'blog/home.html', args)


def blog_post(request, code):
    # article view
    try:
        article = Article.objects.get(pk=code)
        # count view
        article.note_view()

        return render(request, 'blog/post.html', {
            'article': article,
            'categories': Category.objects.all(),
        })
    except Article.DoesNotExist:
        raise Http404()
