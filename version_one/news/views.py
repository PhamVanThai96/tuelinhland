from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import News, Category, NewsTag

def news_list(request):
    """Danh sách tin tức"""
    news_list = News.objects.filter(status='published').select_related('category', 'author')
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news_list = news_list.filter(category=category)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        news_list = news_list.filter(
            Q(title__icontains=search_query) |
            Q(excerpt__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(news_list, 12)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    # Get featured news
    featured_news = News.objects.filter(
        status='published', 
        is_featured=True
    )[:3]
    
    # Get categories
    categories = Category.objects.all()
    
    context = {
        'news': news,
        'featured_news': featured_news,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_slug,
    }
    
    return render(request, 'news/news_list.html', context)

def news_detail(request, slug):
    """Chi tiết tin tức"""
    news = get_object_or_404(News, slug=slug, status='published')
    
    # Increase view count
    news.views_count += 1
    news.save(update_fields=['views_count'])
    
    # Get related news
    related_news = News.objects.filter(
        status='published',
        category=news.category
    ).exclude(id=news.id)[:4]
    
    # Get tags
    tags = NewsTag.objects.filter(newstagrelation__news=news)
    
    context = {
        'news': news,
        'related_news': related_news,
        'tags': tags,
    }
    
    return render(request, 'news/news_detail.html', context)
