from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, PostCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    if request.method=="POST":
        p_form = PostCreationForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Post added successfully.')
            return redirect('index')

    else:
        p_form = PostCreationForm(instance=request.user)
    context ={ 'p_form': p_form}

    return render(request, 'index.html', context)

# For creating users
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
