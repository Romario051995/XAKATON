from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# from .forms import NewsForm
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)
    return render(request, 'home.html')

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