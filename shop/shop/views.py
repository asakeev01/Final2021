from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'products': reverse('product-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'sign-up': reverse('user-create', request=request, format=format),
        # 'bookmark': reverse ('bookmark-detail', request=request, format=format),
    })
    return response