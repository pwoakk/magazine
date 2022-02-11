from django.shortcuts import render
from django.http import Http404
from django.views import generic

from apps.articles.models import Article, ArticleCategory


class ArticleListView(generic.TemplateView):
    """Представление для получения всех публикаций"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['article_list'] = Article.objects.all()
        context['category_list'] = ArticleCategory.objects.all()
        return context


class ArticleDetailView(generic.TemplateView):
    """Представление для получения детальной страницы публикации"""
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = dict()
        article_pk = kwargs['pk']  # primary key который хочет получит клиент
        context['category_list'] = ArticleCategory.objects.all()
        articles_quantity = Article.objects.all().count()
        if article_pk + 1 == articles_quantity:
            next_article_pk = article_pk + 1
        elif (article_pk + 1) % articles_quantity == 0:
            next_article_pk = (article_pk + 1) % articles_quantity
        else:
            next_article_pk = (article_pk+1) % articles_quantity

        if (article_pk - 1) % articles_quantity == 0:
            prev_article_pk = articles_quantity
        else:
            prev_article_pk = (article_pk - 1) % articles_quantity

        context['article_next'] = Article.objects.get(id=next_article_pk)
        context['article_prev'] = Article.objects.get(id=prev_article_pk)
        try:
            context['article'] = Article.objects.get(id=article_pk)

        except Article.DoesNotExist:
            raise Http404
        # context['related'] = context['article'].comments.all()
        return context


class ArticleCategoryDetailListView(generic.TemplateView):
    """Представление для получения всех публикаций"""
    template_name = 'category-single.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['category_list'] = ArticleCategory.objects.all()
        category_pk = kwargs['category_pk']
        context['article_list'] = Article.objects.filter(category_id=category_pk)
        return context


class ArticleCategoryListView(generic.TemplateView):
    """Представление для получения всех публикаций"""
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = dict()
        # category_pk = kwargs['category_pk']
        context['category_list'] = ArticleCategory.objects.all()
        # context['article_list'] = Article.objects.filter(category_id=category_pk)
        return context



