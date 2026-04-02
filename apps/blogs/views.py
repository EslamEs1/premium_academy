from django.shortcuts import get_object_or_404, render

from apps.blogs.models import BlogPageSettings, BlogPost, BlogPostStatus, Category
from apps.main.context_processors import get_singleton_instance
from apps.main.models import CTABlock


def blog_list(request):
    active_category_slug = request.GET.get('category', '').strip()
    page_settings = get_singleton_instance(BlogPageSettings)
    categories = Category.objects.filter(is_active=True).order_by('order', 'name')
    published_posts = BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED).select_related(
        'category',
        'author',
    ).order_by('-published_date', '-created_at')

    filtered_posts = published_posts
    if active_category_slug:
        filtered_posts = filtered_posts.filter(category__slug=active_category_slug)

    featured_post = filtered_posts.filter(is_featured=True).first()
    posts = filtered_posts
    if featured_post is not None:
        posts = posts.exclude(pk=featured_post.pk)

    context = {
        'page_meta': page_settings,
        'page_settings': page_settings,
        'featured_post': featured_post,
        'posts': posts[:6],
        'categories': categories,
        'active_category_slug': active_category_slug,
        'cta': CTABlock.objects.filter(slug='blog-cta', is_active=True).first(),
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost.objects.select_related('category', 'author'),
        slug=slug,
        status=BlogPostStatus.PUBLISHED,
    )

    related_posts = list(
        BlogPost.objects.filter(
            status=BlogPostStatus.PUBLISHED,
            category=post.category,
        )
        .exclude(pk=post.pk)
        .select_related('category', 'author')
        .order_by('-published_date', '-created_at')[:3]
    )
    if len(related_posts) < 3:
        missing_count = 3 - len(related_posts)
        related_posts.extend(
            list(
                BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED)
                .exclude(pk__in=[post.pk, *[item.pk for item in related_posts]])
                .select_related('category', 'author')
                .order_by('-published_date', '-created_at')[:missing_count]
            )
        )

    context = {
        'page_meta': post,
        'post': post,
        'author': post.author,
        'related_posts': related_posts,
        'cta': CTABlock.objects.filter(slug='blog-post-cta', is_active=True).first(),
    }
    return render(request, 'blog-post.html', context)
