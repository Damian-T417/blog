from django import template

from blog.models import Post, Tag

register = template.Library()


@register.filter(name='blog_sidebar')
@register.inclusion_tag('tags/sidebar.html', takes_context=True)
def blog_sidebar_tags(context):
    request = context['request']
    if 'q' in request.GET:
        query = request.GET['q']
    object_list = Tag.objects.filter(post__draft=False).distinct()
    total_post = Post.objects.filter(draft=False).count()
    return locals()
