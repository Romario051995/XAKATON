from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# from .forms import NewsForm
from .models import *


# Create your views here.

# @login_required
def task_list(request):
    task = Task.objects.order_by('-created_at')

    context = {'task': task }
    return render(request, 'task_list.html', context)
    # return render(request, template_name='news/index.html', context=context)


# @login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    context = {'task': task }
    return render(request, 'task_detail.html', context)
    # return render(request, template_name='news/index.html', context=context)


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')

def logout(request):
    logout(request)
    return render(request, 'task_list.html')

# de
# f test(request):
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