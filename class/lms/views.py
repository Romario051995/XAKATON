from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# from .forms import NewsForm
from .models import *


# Create your views here.

# @login_required
def index(request):
    task = Task.objects.order_by('-created_at')

    context = {'task': task }
    return render(request, 'task_list.html', context)
    # return render(request, template_name='news/index.html', context=context)


# def test(request):
#     return HttpResponse('<h1>Test Page</h1>')
#
#
# def add_news(request):
#     if request.method == 'POST':
#         pass
#     else:
#         form = NewsForm()
#     context = {'form': form}
#     return render(request, 'news/add_news.html', context)