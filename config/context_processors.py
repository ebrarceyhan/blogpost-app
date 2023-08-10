from blogpost.models import Category


def global_categories(request):
    context = dict(global_categories=Category.objects.filter(is_active=True))
    return context
