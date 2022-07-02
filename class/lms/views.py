from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


from .models import *
from .forms import *


def home(request):
    return render(request, 'home.html')


@login_required
def task_list(request):
    task = Task.objects.order_by('-created_at')

    context = {'task': task}
    return render(request, 'task_list.html', context)
    # return render(request, template_name='news/index.html', context=context)


@login_required
def task_detail(request, task_id):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        task = get_object_or_404(Task, id=task_id)

        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            Solution.objects.create(student=user, task=task, text=cd['solution'])
            return redirect("home")
    else:
        form = SolutionForm()
        task = get_object_or_404(Task, id=task_id)

        context = {'task': task, 'form': form}
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


@login_required
def marks(request):
    marks = Mark.objects.filter(solution__student=request.user.id)
    marks_values = Mark.objects.filter(solution__student=request.user.id).values_list('mark')
    marks_list = [i[0] for i in marks_values]
    average = sum(marks_list)/len(marks_list)
    context = {'marks': marks, 'average': average}
    print(context)
    return render(request, 'marks.html', context)
