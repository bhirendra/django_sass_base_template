from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def home(request):
    """
    Home page
    :param request:
    :return:
    """
    return render(request, 'index.html')
