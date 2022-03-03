from .models import Category


def product(request):
    categories = Category.objects.all()
    return {'categories': categories}
